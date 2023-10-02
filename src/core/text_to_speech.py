import pyttsx3
import os

def text_to_speech(text:str, to_file:None|str=None):
    
    if not to_file:
        pyttsx3.speak(text)
        return True

    engine = pyttsx3.init()
    engine.save_to_file(text, to_file)
    engine.runAndWait()

    while engine.isBusy():
        pass

    assert os.path.exists(to_file)
    return True
