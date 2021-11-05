from enum import Enum

from tree_sitter import Language

GO_LANGUAGE = Language("languages.so", "go")
JS_LANGUAGE = Language("languages.so", "javascript")
PY_LANGUAGE = Language("languages.so", "python")


class Lang(str, Enum):
    py = "py"
    go = "go"
    js = "js"

    def get_lib(self):
        if self == Lang.py:
            return PY_LANGUAGE
        elif self == Lang.go:
            return GO_LANGUAGE
        elif self == Lang.js:
            return JS_LANGUAGE
