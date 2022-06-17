import os
from enum import Enum

from tree_sitter import Language

so = os.path.join(os.path.dirname(__file__), "language.so")

GO_LANGUAGE = Language(so, "go")
JS_LANGUAGE = Language(so, "javascript")
PY_LANGUAGE = Language(so, "python")
CPP_LANGUAGE = Language(so, "cpp")
C_LANGUAGE = Language(so, "c")


class Lang(str, Enum):
    py = "py"
    go = "go"
    js = "js"
    cpp = "cpp"
    c = "c"

    def get_lib(self):
        if self == Lang.py:
            return PY_LANGUAGE
        elif self == Lang.go:
            return GO_LANGUAGE
        elif self == Lang.js:
            return JS_LANGUAGE
        elif self == Lang.cpp:
            return CPP_LANGUAGE
        elif self == Lang.c:
            return C_LANGUAGE
