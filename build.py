from tree_sitter import Language

Language.build_library(
    "mcc/language.so",
    [
        "vendor/tree-sitter-go",
        "vendor/tree-sitter-javascript",
        "vendor/tree-sitter-python",
        "vendor/tree-sitter-cpp",
        "vendor/tree-sitter-c",
    ],
)


def build(setup_kwargs):
    pass
