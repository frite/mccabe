from distutils.command.build_ext import build_ext  # type:ignore

from tree_sitter import Language


def build(setup_kwargs):
    Language.build_library(
        'languages.so',
        [
            'vendor/tree-sitter-go',
            'vendor/tree-sitter-javascript',
            'vendor/tree-sitter-python'
        ]
    )
    setup_kwargs.update(
        {
            "cmdclass": {"build_ext": build_ext},
        }
    )
