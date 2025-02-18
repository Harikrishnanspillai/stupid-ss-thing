import os
from glob import glob
from ollama import chat
from PIL import Image
from pytesseract import image_to_string as ist

def bot(inp):
    stream = chat(
        model='dolphin-mistral:latest',
        messages=[{'role': 'user', 'content': inp}],
        stream=True,
    )

    for chunk in stream:
      print(chunk['message']['content'], end='', flush=True)
    print('\n\n')

def latestimg():
      dir="C://Users/harik/OneDrive/Pictures/Screenshots 1"
      files=glob(os.path.join(dir, "*.png"))
      if not files:
         print('No files')
         return None
      latest=max(files, key=os.path.getctime)
      return latest

os.system('snippingtool.exe')
latest=latestimg()
img=Image.open(latest)
s=ist(img)
print(f"Orginal:\n{s}")
inp=f"Hey, i used a ocr to get this text from and image, pls go thru it and check and correct any errors(don't remove stuff unless absolutley unnecessary)\n\n{s}"
bot(inp)
os.system(f'del {latest}')

while True:
  msg=input("Enter msg: ")
  bot(msg)
  if msg.lower()=="/bye":
    break
input('Press enter to exit the program')

