import pytesseract as pt
from PIL import Image


def image_to_text(input_path:str, input_lang_code:str)->str:

    if input_lang_code not in pt.get_languages(): raise Exception()

    image = Image.open(input_path)
    x1 = pt.image_to_string(image, lang=input_lang_code)
    return x1
