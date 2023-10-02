import os
from typing import List
from core.config import Config
from pathlib import Path
from argostranslate import package as pk
from argostranslate import translate as tr

def translate(config:Config, input:str, in_lang_name:str, out_lang_name:str)->str:

    if in_lang_name == out_lang_name: return input


    x1 = os.listdir(config.argos_models)
    x2 = [x for x in x1 if x.endswith('.argosmodel')]

    x3 = [os.path.join(config.argos_models,x) for x in x2]
    for x in x3: pk.install_from_path(Path(x))
    
    langs = tr.get_installed_languages()
    in_lang = get_lang(langs, in_lang_name)
    out_lang = get_lang(langs, out_lang_name)

    assert in_lang
    assert out_lang

    tranlator = in_lang.get_translation(out_lang)
    assert tranlator
    
    return tranlator.translate(input)

def get_lang(langs:List[tr.Language], lang_name):
    return next((x for x in langs if str(x).lower() == lang_name.lower()), None)
