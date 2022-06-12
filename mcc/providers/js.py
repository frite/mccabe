from mcc.languages import Lang
from mcc.providers import Mccabe


class MccabeJS(Mccabe):
    suffixes = (".js",)
    language = Lang.js
    judge_nodes = [
        "if_statement",
        "while_statement",
        "for_statement",
        "catch_clause",
        "with_statement",
        "function_declaration",
        "&&",
        "||",
    ]
