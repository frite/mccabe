from typing import Type

from CyclomaticComplexity.exceptions import LanguageNotSupportException
from CyclomaticComplexity.languages import Lang
from CyclomaticComplexity.providers import CyclomaticComplexity
from CyclomaticComplexity.providers.go import CyclomaticComplexityGo
from CyclomaticComplexity.providers.js import CyclomaticComplexityJS
from CyclomaticComplexity.providers.python import CyclomaticComplexityPy


def get_provider_class(lang: Lang) -> Type[CyclomaticComplexity]:
    if lang == Lang.py or lang == Lang.python:
        return CyclomaticComplexityPy
    elif lang == Lang.go or lang == Lang.golang:
        return CyclomaticComplexityGo
    elif lang == Lang.js or lang == Lang.javascript:
        return CyclomaticComplexityJS
    else:
        raise LanguageNotSupportException(f"The language {lang} is not supported")
