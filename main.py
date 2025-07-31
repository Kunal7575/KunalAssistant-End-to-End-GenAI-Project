import streamlit as st
import base64
from langchain_helper import get_qa_chain, create_vector_db


# Set blurred background with dark overlay
def set_background(image_path):
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("data:image/webp;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .main-container {{
        max-width: 800px;
        margin: 0 auto;
        padding: 2rem;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Page settings
st.set_page_config(page_title="Kunal Assistant", page_icon="🤖")

# Set background
set_background("assets/bg.webp")

# Stylish input + button CSS
st.markdown("""
    <style>
    .stTextInput>div>div>input {
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
        border: 1.5px solid #00ffff;
    }
    .stTextInput>div>div>input:focus {
        border: 2px solid #00ccff;
        outline: none;
    }

    .stButton>button {
        background: linear-gradient(to right, #00ff88, #00cc66);
        color: black;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.7em 1.5em;
        font-size: 16px;
        border: none;
        box-shadow: 0 0 12px #00ff8855;
        transition: all 0.3s ease-in-out;
    }

    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 16px #00ff88aa;
    }

    .stMarkdown h1 {{
        color: #00ff88;
        font-size: 2.5rem;
        text-align: center;
        margin-top: 1.5rem;
    }}
    .stMarkdown h3, .stMarkdown h4 {{
        color: #ffffff;
        text-align: center;
    }}
    </style>
""", unsafe_allow_html=True)

# Main layout
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

st.markdown("# 🤖 Kunal's AI Assistant")
st.markdown("Ask me anything about Kunal’s projects, skills, or background. I’m trained on his resume and portfolio!")

if st.button("Create Vector Database"):
    create_vector_db()
    st.success("Knowledgebase created!")

query = st.text_input("💬 Type your question here")

if query:
    chain = get_qa_chain()
    with st.spinner("Thinking..."):
        response = chain.invoke({"query": query})
        st.markdown("### Answer")
        st.write(response["result"])

        with st.expander("📄 View Source Context"):
            for doc in response["source_documents"]:
                st.markdown(doc.page_content)

st.markdown("</div>", unsafe_allow_html=True)
