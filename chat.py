import os
from dotenv import load_dotenv

from langchain_qdrant import QdrantVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from openai import OpenAI

load_dotenv()

openai_client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    api_key=os.getenv("GEMINI_API_KEY")
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="rag_project",
    embedding=embedding_model,
)

user_query = input("Ask Something: ")

search_result = vector_db.similarity_search(query=user_query)

context = "\n\n\n".join(
    [
        f"Page Content: {result.page_content}\n"
        f"Page Number: {result.metadata['page_label']}\n"
        f"File Location: {result.metadata['source']}"
        for result in search_result
    ]
)

system_prompt = f"""
You are a helpful AI assistant that answers the user's query only using the retrieved PDF context.

Instructions:
- Answer only from the provided context.
- If the answer is not present in the context, say:
  "I couldn't find the answer in the provided PDF."
- Mention the relevant page number whenever possible.

Context:
{context}
"""

response = openai_client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_query},
    ],
)

print(response.choices[0].message.content)