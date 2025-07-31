# langchain_helper.py

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.document_loaders import CSVLoader

from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI

from secret_key import api_key

# Constants
vectordb_file_path = "kunal_faiss_db"
instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")

# Create the FAISS vector DB
def create_vector_db():
    import pandas as pd
    from langchain.docstore.document import Document

    df = pd.read_csv("kunal_faq_questions.csv")

    docs = []
    for _, row in df.iterrows():
        combined = f"Question: {row['prompt']}\nAnswer: {row['response']}"
        docs.append(Document(page_content=combined))

    print(f"📄 Loaded {len(docs)} documents into vector DB")
    vectordb = FAISS.from_documents(docs, instructor_embeddings)
    vectordb.save_local(vectordb_file_path)



# Define the prompt template
def get_prompt():
    prompt_template = """You are an AI assistant answering based only on the given context.

Context:
{context}

Question:
{question}

Answer:
"""
    return PromptTemplate(template=prompt_template, input_variables=["context", "question"])


# Build the QA chain
def get_qa_chain():
    vectordb = FAISS.load_local(vectordb_file_path, instructor_embeddings, allow_dangerous_deserialization=True)
    retriever = vectordb.as_retriever(search_type="mmr", search_kwargs={"k": 3})

    prompt = get_prompt()
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt},  # ✅ prompt is now passed correctly
        input_key="query"
    )
    return qa_chain

# CLI test (optional)
if __name__ == "__main__":
    create_vector_db()
    # chain = get_qa_chain()
    # result = chain.invoke({"query": "What is Kunal's work experience?"})
    # print(result["result"])
