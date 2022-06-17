from mcc.languages import Lang
from mcc.providers import Mccabe


class MccabeC(Mccabe):
    suffixes = (".c", ".h")
    language = Lang.c
    judge_nodes = [
        "if_statement",
        "case_statement",
        "do_statement",
        "for_range_loop",
        "for_statement",
        "goto_statement",
        "function_declarator",
        "pointer_declarator",
        "struct_specifier",
        "preproc_elif",
        "while_statement",
        "switch_statement",
        "&&",
        "||",
    ]
