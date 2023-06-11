# <samp>Screenshot to Text</samp>

<samp>Python program to extract text from a screenshot image and optionally query it to ChatGPT.</samp>


<samp> Install Dependencies </samp>
------------
```
$ python3 -m pip install openai tesseract pyautogui pyperclip
```
<samp> This program uses scrot to take screenshots, so you may need to install scrot on your Linux desktop. </samp>
```
$ sudo apt install scrot
```

<samp> Guide </samp>
------------
```
optional arguments:
  -h, --help  Show this help message and exit
  -q          Query the extracted text to ChatGPT
  -c          Copy the extracted text to clipboard
```
