from typing import Any, Dict

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from backend.agent.state import AgentState
from backend.agent.nodes import NavigatorAgent, SummaryAgent
from backend.database.models import Place



class CustomAgent:
    def __init__(self, llm_model_name:str="qwen2.5:7b", config=None):
        self.config= config or {"configurable": {"thread_id": "1"}}
        self.llm_model_name= llm_model_name
        self.build_graph()

    def build_graph(self, ):

        _builder = StateGraph(AgentState)
        _builder.add_node("director_agent", NavigatorAgent(llm_model_name=self.llm_model_name, config=self.config))
        _builder.add_node("summary_agent", SummaryAgent(llm_model_name=self.llm_model_name, config=self.config))

        _builder.add_edge(START, "director_agent")
        _builder.add_edge("director_agent", "summary_agent")
        _builder.add_edge("summary_agent", END)

        self.graph = _builder.compile(checkpointer=InMemorySaver())



    def invoke_graph(self, input_data: Dict[str, Any]):
        final_state = self.graph.invoke(input_data, config=self.config)
        return final_state["all_messages"][-1].content


if __name__ == '__main__':
    _graph = CustomAgent()


    _graph.invoke_graph(
        input_data={
            "departure": Place(name="dep", description="", place_id="") ,
            "destination": Place(name="des", description="", place_id=""),
            "current_place": Place(name="current", description="", place_id="")
        })

    # _graph.invoke_graph(
    #     input_data={
    #         "departure": Place(name="1", description="1", place_id="1"),
    #         "destination": Place(name="2", description="2", place_id="2")
    #     })


