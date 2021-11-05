import os
from typing import List, Optional

from tree_sitter import Node, Parser, Tree

from mcc.exceptions import LanguageNotSupportException, ParamMissingException
from mcc.languages import Lang


class Mccabe:
    suffix: str
    language: Lang
    judge_nodes: List[str]

    def __init__(
        self,
        directory: Optional[str] = None,
        file: Optional[str] = None,
    ):
        """
        The order of param is source > file > directory
        :param directory: The source language
        :param file: The source code file
        """
        if not any([directory, file]):
            raise ParamMissingException(
                "You must specify a source code file or directory or raw source code"
            )
        try:
            lib = self.language.get_lib()
        except AttributeError:
            raise LanguageNotSupportException(f"The language {self.language} is not supported")
        self.directory = directory
        self.file = file
        self.parser = Parser()
        self.parser.set_language(lib)

    def _source_codes(self):
        if self.file:
            with open(self.file) as f:
                yield self.file, f.read()
        elif self.directory:
            for root, dirs, files in os.walk(self.directory):
                for file in files:
                    if not file.endswith(self.suffix):
                        continue
                    path = os.path.join(root, file)
                    with open(path) as f:
                        yield path, f.read()

    def _visit_node(self, node: Node):
        count = 0
        if node.type in self.judge_nodes:
            count += 1
        for item in node.children:
            count += self._visit_node(item)
        return count

    def complexity(self):
        for file, code in self._source_codes():
            tree = self.parser.parse(code.encode())  # type:Tree
            yield file, self._visit_node(tree.root_node)

    def run(self):
        ret = {}
        for file, count in self.complexity():
            ret[file] = count
        return ret
