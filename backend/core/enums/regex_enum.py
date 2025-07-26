from enum import Enum


class RegexEnum(Enum):
    NAME=(
        r'^[A-Z][a-zA-Z ]{,29}$',
        'Only alpha characters are allowed.'
    )

    def __init__(self, pattern:str, msg:str):
        self.pattern = pattern
        self.msg = msg