import streamlit as st
import google.generativeai as genai
import os

# Configurar a API do Gemini
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ A variável de ambiente GEMINI_API_KEY não está definida.")
else:
    genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-pro")

st.set_page_config(page_title="Agente BlinkClinic", page_icon="🩺")

st.title("🩺 Agente BlinkClinic - Powered by Gemini")
st.write("Treina o agente fazendo perguntas ou simulando cenários clínicos.")

# Caixa de input
user_input = st.text_area("Escreve a tua pergunta ou cenário:")

# Botão
if st.button("Enviar"):
    if user_input.strip():
        with st.spinner("A pensar..."):
            try:
                response = model.generate_content(user_input)
                st.subheader("Resposta do agente:")
                st.write(response.text)
            except Exception as e:
                st.error(f"❌ Erro ao contactar o modelo: {e}")
    else:
        st.warning("Por favor escreve uma pergunta.")

