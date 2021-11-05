from distutils.command.build_ext import build_ext  # type:ignore

from tree_sitter import Language

Language.build_library(
    'mcc/language.so',
    [
        'vendor/tree-sitter-go',
        'vendor/tree-sitter-javascript',
        'vendor/tree-sitter-python'
    ]
)


def build(setup_kwargs):
    setup_kwargs.update(include_package_data=True)
