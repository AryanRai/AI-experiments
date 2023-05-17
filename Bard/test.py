
import bardapi
import os
from TTS.api import TTS# import required module
import sounddevice as sd
import string
import nltk.data
import time
sps = 48000
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
    model_name = "tts_models/en/jenny/jenny"
    tts = TTS(model_name, gpu=True)
    wav = tts.tts(text=new_s)
    
    # for playing note.mp3 file
    sd.wait()
    sd.play(wav, samplerate=sps)
    


    # List available 🐸TTS models and choose the first one
    #for i in TTS.list_models():
    #   print(i)

    #usable models
    #tts_models/en/ljspeech/tacotron2-DCA

    #tts_models/en/ljspeech/fast_pitch

    #tts_models/en/jenny/jenny


while True:
    input_text = input(input_name + ": ")
    response = bardapi.core.Bard(timeout=10).get_answer(input_text)
    print("Bard: " + response['content'])
    lst = tokenizer.tokenize(response['content'])
    for i in lst:
        speak(i)
        time.sleep(1)


