from core.config import Config
from vosk import KaldiRecognizer, Model
import os
import wave
import json

def speech_to_text(config:Config, input_path:str, input_lang:str)->str:

    assert os.path.exists(input_path)
    wf = wave.open(input_path, 'rb')

    model_path = os.path.join(config.vosk_models, input_lang) + '.model'
    assert os.path.exists(model_path)
    model = Model(model_path)

    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)
    data = wf.readframes(wf.getnframes())
    rec.AcceptWaveform(data)
    r2 = rec.Result()
    text = json.loads(r2)['text']
    return text
