from langchain_ollama.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
# from backend.agent.prompts import SYSTEM_PROMPT, TEST_USER_PROMPT


class OllamaLLM:
    def __init__(self, model_name: str="qwen3:8b", base_url:str="http://localhost:11434", temperature=0.0):
        # self.model_name = model_name
        # self.base_url = base_url
        # self.temperature = temperature
        self.llm = ChatOllama(base_url=base_url, model=model_name, temperature=temperature)


    def call_agent(self, user_msg:str, sys_msg:str=None):
        if sys_msg is None:
            response = self.llm.invoke([HumanMessage(user_msg)])
        else:
            response = self.llm.invoke([SystemMessage(sys_msg), HumanMessage(user_msg)])

        return response.content

#
    @classmethod
    def from_config(cls, model_name:str="qwen2.5:7b"):
        return cls(model_name=model_name)


if __name__ == '__main__':
    tst = OllamaLLM.from_config()
    # print(tst.call_agent(user_msg="Hello, world!"))
    print(tst.call_agent(user_msg=TEST_USER_PROMPT, sys_msg=SYSTEM_PROMPT))