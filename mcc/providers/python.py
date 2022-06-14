from mcc.languages import Lang
from mcc.providers import Mccabe


class MccabePy(Mccabe):
    suffixes = (".py",)
    language = Lang.py
    judge_nodes = [
        "if_statement",
        "elif_clause",
        "while_statement",
        "for_statement",
        "except_clause",
        "boolean_operator",
        "with_statement",
        "assert_statement",
        "list_comprehension",
        "function_definition",
    ]
