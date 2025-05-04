from google.adk.tools import google_search
from google.adk.agents import LlmAgent 
from .utils import load_instruction


# import google.generativeai as genai

# # Print for debugging
# print(genai, 'aaaaaaaaaaaaaaaaaaaaaaaa')

# # Configure with your API key
# genai.configure(api_key="AIzaSyBYUcl40jdMsB65S0xOCYsJk1Mnhz9JxtA")

# # List all available models
# try:
#     models = genai.list_models()  # List models from the API
#     for model in models:
#         print(model.name)  # Print each model's name
# except Exception as e:
#     print("Error fetching models:", e)

malayalam_news_agent = LlmAgent(

    name='malayalam_news_agent',
    model='gemini-2.0-flash-exp',
    description='agent that seaches the lastest news and summerize in malayalam',
    instruction=load_instruction('Instruction.txt'),
    tools=[google_search]

)

root_agent = malayalam_news_agent