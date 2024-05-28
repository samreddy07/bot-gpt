import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyCywxL3BTdCMWt22qmZIxpOJVECFNbr02s")
model = genai.GenerativeModel('gemini-1.5-pro-latest')

def get_gemini_response(input):
  response = model.generate_content([input])
  return response.text

response = ''

def make_request(question_input: str):
    response = get_gemini_response(question_input)
    return response

st.title("💬 Sambot")
st.caption("🚀 A Streamlit Sambot powered by GeminiApi")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = make_request(prompt)
    msg = response
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
