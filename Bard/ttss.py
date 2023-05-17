from gtts import gTTS
from io import BytesIO
from pygame import mixer
import time
mixer.init()

def speak(text):
    mp3_fp = BytesIO()
    tts = gTTS(text, lang='en', tld='us')
    tts.write_to_fp(mp3_fp)
    sound = mp3_fp
    sound.seek(0)
    if (mixer.music.get_busy() == False): 
        mixer.music.load(sound, "mp3")
        mixer.music.play()
    else :
        mixer.music.queue(sound, "mp3")
    
speak('hi')

speak("how are u doing")
time.sleep(10)



