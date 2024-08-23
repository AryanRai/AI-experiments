
import bardapi
import os
from TTS.api import TTS# import required module
import sounddevice as sd
import string
import nltk.data
import time
from gtts import gTTS
from io import BytesIO
from pygame import mixer
import time
mixer.init()


# set your __Secure-1PSID value to key
os.environ['_BARD_API_KEY']="WQg5a8FOKayi6mwHAJ3GY5Nw-vFvjcw0rYbN6_qwaHtrErj6TIjObOaMO_w4edWsL281uw."

# set your input text
input_name = input("enter your name:")

whitelist = string.ascii_letters + string.digits + ' ' + '.' + ',' + '!' + '?' + '"' + "'"
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# Send an API request and get a response.


def speak(text):
    new_s = ''
    for char in text:
        if char in whitelist:
            new_s += char
        else:
            new_s += ' '
    mp3_fp = BytesIO()
    tts = gTTS(new_s, lang='en', tld='us')
    tts.write_to_fp(mp3_fp)
    sound = mp3_fp
    sound.seek(0)
    if (mixer.music.get_busy() == False): 
        mixer.music.load(sound, "mp3")
        mixer.music.play()
    else :
        mixer.music.queue(sound, "mp3")


while True:
    input_text = input(input_name + ": ")
    response = bardapi.core.Bard(timeout=10).get_answer(input_text)
    print("Bard: " + response['content'])
    lst = tokenizer.tokenize(response['content'])
    for i in lst:
        speak(i)
        time.sleep(1)

