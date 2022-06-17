from functools import lru_cache
from typing import Type

from mcc.exceptions import LanguageNotSupportException
from mcc.languages import Lang
from mcc.providers import Mccabe


# should import these when use __subclasses__
from mcc.providers.go import MccabeGo  # noqa:F401
from mcc.providers.js import MccabeJS  # noqa:F401
from mcc.providers.python import MccabePy  # noqa:F401
from mcc.providers.c import MccabeC  # noqa:F401
from mcc.providers.cpp import MccabeCPP  # noqa:F401


@lru_cache()
def get_provider_class(lang: Lang) -> Type[Mccabe]:
    for cls in Mccabe.__subclasses__():
        if cls.language == lang:
            return cls
    else:
        raise LanguageNotSupportException(f"The language {lang} is not supported")
