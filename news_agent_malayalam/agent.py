from google.adk.tools import google_search
from google.adk.agents import LlmAgent 

malayalam_news_agent = LlmAgent(

    name='malayalam_news_agent',
    model='gemini-2-0-flash-exp',
    description='agent that seaches the lastest news and summerize in malayalam',
    instruction='ai agent '

)