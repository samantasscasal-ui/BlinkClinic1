
import streamlit as st
import google.generativeai as genai
import os

# Configurar a API do Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

st.set_page_config(page_title="Agente BlinkClinic", page_icon="💬")

st.title("💬 Agente BlinkClinic – Powered by Gemini")

st.write("Treina o agente fazendo perguntas ou simulando cenários clínicos.")

# Caixa de input
user_input = st.text_area("Escreve a tua pergunta ou cenário:")

# Botão
if st.button("Enviar"):
    if user_input.strip():
        with st.spinner("A pensar..."):
            response = model.generate_content(user_input)
        st.subheader("Resposta do agente:")
        st.write(response.text)
    else:
        st.warning("Por favor escreve uma pergunta.")

