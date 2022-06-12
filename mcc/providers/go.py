from mcc.languages import Lang
from mcc.providers import Mccabe


class MccabeGo(Mccabe):
    suffixes = (".go",)
    language = Lang.go
    judge_nodes = [
        "if_statement",
        "for_statement",
        "function_declaration",
        "expression_case",
        "for_statement",
        "&&",
        "||",
    ]
