import dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv('../.env')

chat_model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)