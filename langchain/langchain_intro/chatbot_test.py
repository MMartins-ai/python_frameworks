from chatbot import review_chain
from chatbot import hospital_agent_executor
#question = """Has anyone complained about
 #           communication with the hospital staff?"""

#resposta =review_chain.invoke(question)

#print(resposta)
#resposta = chat_model.invoke(messages)
"""
resposta = chat_model.stream(messages)
for s in resposta:
    print(s.content, end="", flush=True)
"""

hospital_agent_executor.invoke({"input": "What have patients said about their comfort at the hospital?"})