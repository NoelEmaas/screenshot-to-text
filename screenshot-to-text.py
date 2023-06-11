import argparse
import openai
import platform
import os
import pytesseract
import pyperclip
from PIL import Image

openai.api_key = '(your_api_key_here)'

def query_to_chatgpt(prompt):
    _model = "gpt-3.5-turbo"
    _messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model=_model,
        messages=_messages,
    )

    return response.choices[0].message["content"]

def extract_text_from_image(image_path):
    with Image.open(image_path) as image:
        text = pytesseract.image_to_string(image)
        return text

def take_screenshot():
    os.system(f"scrot -s ss-to-text.png")
    image_path = "ss-to-text.png"
    return image_path

def main():
    parser = argparse.ArgumentParser(description='Script to extract text from an image and optionally query it to ChatGPT.')
    
    parser.add_argument('-q', action='store_true', help='Query the extracted text to ChatGPT')
    parser.add_argument('-c', action='store_true', help='Copy the extracted text to clipboard')

    args = parser.parse_args()

    image_path = take_screenshot()
    extracted_text = extract_text_from_image(image_path)

    if args.c:
        pyperclip.copy(extracted_text)
        print("Extracted text copied to clipboard!")

    if args.q:
        response = query_to_chatgpt(extracted_text)
        print(response)

    if not args.c and not args.q:
        print("Extracted Text:")
        print(extracted_text)

    os.remove(image_path)

if __name__ == "__main__":
    main()
