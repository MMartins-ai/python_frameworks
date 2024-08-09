from langchain.schema.messages import HumanMessage, SystemMessage
from chatbot import chat_model

messages = [
    SystemMessage(
        content=  """You are an assistant knowledgeable about
        healthcare. Only answer healthcare-related questions."""
    ),
    HumanMessage(content="What is Medicaid managed care?")
]

#resposta = chat_model.invoke(messages)
resposta = chat_model.stream(messages)
for s in resposta:
    print(s.content, end="", flush=True)