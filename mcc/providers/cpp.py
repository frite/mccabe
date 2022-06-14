from mcc.languages import Lang
from mcc.providers import Mccabe


class MccabeCPP(Mccabe):
    suffixes = (".cc", ".cpp", ".cxx", ".h")
    language = Lang.cpp
    judge_nodes = [
        "if_statement",
        "case_statement",
        "do_statement",
        "for_range_loop",
        "for_statement",
        "goto_statement",
        "function_declarator",
        "pointer_declarator",
        "class_specifier",
        "struct_specifier",
        "preproc_elif",
        "while_statement",
        "switch_statement",
        "&&",
        "||",
    ]
