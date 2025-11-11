!pip install google-generativeai

import google.generativeai as genai
import time

genai.configure(api_key="YOUR_API_KEY")
model=genai.GenerativeModel("gemini-2.5-flash")
print("Gemini chatbot | type 'exit' to quit\n")

while True:
  user_input=input("You: ")

  if user_input.lower()=="exit":
    print("Gemini: Goodbye!")
    break

  try:
    stream=model.generate_content(user_input,stream=True)
    print("Gemini:",end="",flush=True)
    for chunk in stream:
        print(chunk.text,end="",flush=True) 
        time.sleep(0.1) 
    print("\n")

  except Exception as e:
    print("ERROR",e)
