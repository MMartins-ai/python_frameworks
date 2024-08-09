from chatbot import review_chain

context = "I had a great Stay"
question = "Did anyone have a positive experience?"

resposta =review_chain.invoke({
    "context": context,
    "question": question
})

print(resposta)
#resposta = chat_model.invoke(messages)
"""
resposta = chat_model.stream(messages)
for s in resposta:
    print(s.content, end="", flush=True)
"""