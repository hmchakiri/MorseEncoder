'''
    File name: main.py
    Author: Haytham Chakiri
    Date created: 02/11/2021
'''
from pydub import AudioSegment as audio

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ', ':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-',  "'":'.----.',
   ',':'--..--'
}
def encryption(message):
    message = message.upper()
    my_cipher = ''
    for myletter in message:
        if myletter != ' ':
            my_cipher += MORSE_CODE_DICT[myletter] 
            my_cipher += '__'
        if (myletter == ' '):
            my_cipher += '____'
        
    return my_cipher

text = input("What's the message ?")
msg = encryption("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum")
hyphen = audio.from_wav("hyphen.wav")
dot = audio.from_wav("sdot.wav")
none = audio.from_wav("none.wav")



print(msg)

combined_sounds = none

for element in msg:
    if (element == "-"):
        combined_sounds += hyphen + none
        print('1')
    if (element == "."):
        print('0')
        combined_sounds += dot + none
    if (element == "_"):
        print("_")
        combined_sounds += none

combined_sounds.export("path.wav", format="wav")
