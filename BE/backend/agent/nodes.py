from backend.agent.llm_config import OllamaLLM
from backend.agent.state import AgentState
from langchain_core.messages import AIMessage
import json

class NavigatorAgent:
    SYSTEM_PROMPT = """You are helpful assistant in navigation.
    you will be provided information about the target destination, you have to make it user friendly navigation.

    IMPORTANT RULE:
    - Never make up information, always use provided information.
    - info related to the traversed places are just for additional info, do not mention "already passed through" unless are needed by user.
    - Target language is English, respond in English.

    output structure:
    - output must be plane text.
    """

    TEST_USER_PROMPT = """from here to you destination you have 10 meter to pass, in your way to next place you well have one big painting and there is huge stature next to last door on right!"""

    def __init__(self, llm_model_name:str="qwen2.5:7b", config=None):
        self.llm = OllamaLLM(model_name=llm_model_name)
        # self.llm = OllamaLLM.from_config(model_name=llm_model_name)

        self.config = config

    def call_agent(self, user_prompt:str, system_prompt:str):
        result = self.llm.call_agent(user_prompt, system_prompt)
        return result

    def __call__(self, state:AgentState):
        print("state in Navigator agent", state)
        # current_place = state.current_place.description
        # try:
        #     current_place = state.traversed_places[-2].description
        # except Exception as e:
        #     print(f"in exception, {e}")
        #     current_place = state.current_place.description

        current_place = state.traversed_places[-2].description
        next_place = state.traversed_places[-1].description
        traversed_so_far = state.traversed_places[:-1]
        more_context = "\n".join(
            [
                f"name:{place.name}, description:{place.description}, floor:{place.floor + 1}, section:{place.section}"
                for place in traversed_so_far
            ]
        )
        if state.traversed_places[-1].place_id != state.destination.place_id:
            user_prompt = (f"Current place is {current_place}, Next place is {next_place}."
                           f"for more context here is the traversed places so far: \n{more_context} ")
        else:
            user_prompt = (f"with taking this step, user reaches the destination, at the end give a summary."
                           f"Current place is {current_place}, Next place is {next_place}."
                           f"for more context here is the traversed places so far: \n{more_context} ")

        print("user_prompt", user_prompt)
        response = self.call_agent(user_prompt, self.SYSTEM_PROMPT)
        print(response, response)
        return {"all_messages": AIMessage(content=response), }


class SummaryAgent:
    def __init__(self, llm_model_name: str = "qwen2.5:7b", config=None):
        self.llm = OllamaLLM(model_name=llm_model_name)
        # self.llm = OllamaLLM.from_config(model_name=llm_model_name)

        self.config = config

    def call_agent(self, user_prompt:str, system_prompt:str):
        result = self.llm.call_agent(user_prompt, system_prompt)
        return result

    def __call__(self, state: AgentState):

        if state.traversed_places[-1].place_id == state.destination.place_id:
            pass # if we want we can prepare summary here


        print("state in summary agent", state)
        return {}


