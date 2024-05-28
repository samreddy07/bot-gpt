import google.generativeai as genai

genai.configure(api_key="AIzaSyCywxL3BTdCMWt22qmZIxpOJVECFNbr02s")
model = genai.GenerativeModel('gemini-1.5-pro-latest')
model_video = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")

def get_gemini_response(input):
  response = model.generate_content([input])
  return response.text