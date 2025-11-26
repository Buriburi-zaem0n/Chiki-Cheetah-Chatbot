import os
import google.generativeai as genai

print("google-generativeai version:", genai.__version__)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("Available models:")
for m in genai.list_models():
    print("-", m.name)
