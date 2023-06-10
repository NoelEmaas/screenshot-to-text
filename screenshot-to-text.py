import openai
import platform
import os
import pytesseract
import pyperclip
from PIL import Image

openai.api_key = '(Your API key here)'

def query_to_chatgpt(prompt):
    _model = "gpt-3.5-turbo"
    _messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create (
        model = _model,
        messages = _messages,
    )
    
    return response.choices[0].message["content"]

def extract_text_from_image(image_path):
    with Image.open(image_path) as image:
        text = pytesseract.image_to_string(image)
        return text

def main():
    os.system(f"scrot -s screenshot.png")
    image_path = "screenshot.png"

    extracted_text = extract_text_from_image(image_path)
    pyperclip.copy(extracted_text)
    print("Extracted text copied to clipboard!")
    os.system(f"rm screenshot.png")

    response = query_to_chatgpt(extracted_text)
    print(response)

if __name__ == "__main__":
    main()
