# test_rag.py
import streamlit as st
from langchain_ollama import OllamaLLM

st.set_page_config(page_title="PhantomPrompt Test Target")
st.title("⚡ PhantomPrompt – Test RAG (Llama 3.2)")
st.caption("Bu sayfayı taramak için http://localhost:8501 kullan")

model = OllamaLLM(model="llama3.2:latest")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Buraya mesaj yaz..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    with st.chat_message("assistant"):
        response = model.invoke(prompt)
        st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})