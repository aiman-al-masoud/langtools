from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    argos_models:str = '/home/aiman/code/translator/res/models/argos'
    vosk_models:str = '/home/aiman/code/translator/res/models/vosk'
    test_data:str = '/home/aiman/code/translator/res/test-data'
    tmp:str = '/home/aiman/code/translator/res/tmp'

    @classmethod
    @property
    def config(cls):
        return cls()
