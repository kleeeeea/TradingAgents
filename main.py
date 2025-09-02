import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from p24_code.agentic_code.langchain1.init import init_langchain_model

init_langchain_model()
os.environ['FINNHUB_API_KEY'] = 'd2i3sf9r01qucbnn1on0d2i3sf9r01qucbnn1ong'
load_dotenv(dotenv_path=("/Users/l/git_repos/p24-backend/.env"), override=True)

from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# Create a custom config
config = DEFAULT_CONFIG.copy()
config["deep_think_llm"] = "gpt-4.1-mini"  # Use a different model
config["quick_think_llm"] = "gpt-4.1-mini"  # Use a different model
config["max_debate_rounds"] = 1  # Increase debate rounds
config["online_tools"] = True # Use online tools or cached data

# Initialize with custom config
ta = TradingAgentsGraph(debug=True, config=config, selected_analysts=["market"])
ChatOpenAI._generate_with_cache
# forward propagate
_, decision = ta.propagate("NVDA", "2024-05-10")
print(decision)
