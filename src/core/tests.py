import pathlib
from core.config import Config

# extracting text from image
def test1():
    from core.image_to_text import image_to_text
    x = image_to_text(Config.config.test_data+'/'+'test1.png', 'eng').replace('\n', ' ').strip()
    assert x == 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness...'

# translating from lang1 to lang2
def test2():
    from core.translate import translate
    x = translate(Config.config, 'ciao a tutti!', 'italian', 'english')
    assert x == 'Hello, everyone!'

# "translating" from lang1 to lang1
def test3():
    from core.translate import translate
    x = translate(Config.config, 'ciao a tutti!', 'italian', 'italian')
    assert x == 'ciao a tutti!'

# recognizing voice
def test4():
    from core.speech_to_text import speech_to_text
    x = speech_to_text(Config.config, Config.config.test_data+'/'+'hello-world.wav', 'en')
    assert x == "hi hello world i'm stupid"

# text to speech generate audio file
def test5():
    from core.text_to_speech import text_to_speech
    from core.speech_to_text import speech_to_text
    file_path = Config.config.tmp+'/'+'speech.wav'
    pathlib.Path(file_path).unlink(missing_ok=True)
    text1 = 'hello world'
    text_to_speech(text1, to_file=file_path)
    text2 = speech_to_text(Config.config, file_path, 'en')
    assert text1 == text2