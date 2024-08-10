import dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

REVIEWS_CHROMA_PATH = "chroma_data/"

dotenv.load_dotenv('../.env')

reviews_vector_db = Chroma(
    persist_directory = REVIEWS_CHROMA_PATH,
    embedding_function = OpenAIEmbeddings(),
)

question = """Has anyone complained about
            communication with the hospital staff?"""

relevant_docs = reviews_vector_db.similarity_search(question, k=3)

print(relevant_docs[0].page_content)
print(relevant_docs[1].page_content)
print(relevant_docs[2].page_content)