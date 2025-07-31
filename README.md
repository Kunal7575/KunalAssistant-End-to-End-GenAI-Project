# **Kunal’s AI Assistant** 🤖  
An **AI-powered personal assistant** trained exclusively on my resume, portfolio, and professional achievements.  
Ask it questions about my background, technical projects, skills, and more — and it will answer with **contextual, accurate, and relevant details**.  

---

## **📌 Features**
- **Custom Knowledge Base** – Answers only from my personal career data (no hallucinations).
- **LangChain Integration** – For prompt handling, chaining, and retrieval.
- **Vector Database (FAISS)** – Fast similarity search for relevant information.
- **HuggingFace Embeddings** – Uses `hkunlp/instructor-large` for high-quality semantic embeddings.
- **Google Gemini LLM** – Generates natural, human-like answers.
- **Streamlit Frontend** – Clean, interactive web interface.

---

## **🛠 Tech Stack**
| Component         | Technology |
|------------------|------------|
| **Language**     | Python |
| **Framework**    | Streamlit |
| **LLM**          | Google Gemini (`gemini-1.5-flash`) |
| **Vector Store** | FAISS |
| **Embeddings**   | HuggingFace `hkunlp/instructor-large` |
| **Orchestration**| LangChain |
| **Data Loader**  | LangChain CSVLoader |

---

## **⚙ How It Works**
1. **CSV Knowledge Base**  
   - All Q&A pairs about me are stored in a CSV file (`kunal_faq_questions.csv`).  
   - Each row contains:
     - `prompt` → The question  
     - `response` → The detailed answer  

2. **Embedding Creation**  
   - `create_vector_db()` reads the CSV and **combines each question & answer** into one text block.  
   - Generates embeddings using HuggingFace’s `hkunlp/instructor-large`.  
   - Stores them in a **FAISS vector store** (`kunal_faiss_db`).

3. **Query Handling**  
   - User asks a question in the Streamlit app.  
   - LangChain retrieves the **most relevant chunks** from FAISS.  
   - Google Gemini LLM formulates the final answer using the retrieved context.  

4. **Response**  
   - The answer is displayed in the UI.  
   - Source context can be expanded for transparency.

---

## **📂 Project Structure**
📦 kunal-ai-assistant
├── main.py # Streamlit frontend
├── langchain_helper.py # Core LangChain logic
├── kunal_faq_questions.csv # Personal Q&A knowledge base
├── assets/ # Background images & styles
├── secret_key.py # API keys (not in GitHub)
└── kunal_faiss_db/ # Vector database (generated)






