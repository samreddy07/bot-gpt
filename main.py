import streamlit as st
from models import get_gemini_response

response = ''

def make_request(question_input: str):
    response = get_gemini_response(question_input)
    return response

st.title("SAM ChatGPT")

st.markdown("""---""")

question_input = st.text_area("Enter question")
rerun_button = st.button("Get Response")

st.markdown("""---""")

if question_input:
    response = make_request(question_input)
else:
    pass

if rerun_button:
    response = make_request(question_input)
else:
    pass

if response:
    st.write("Response:")
    st.write(response)
else:
    pass
