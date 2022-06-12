import multiprocessing
import os
from typing import List, Optional, Tuple

from tree_sitter import Node, Parser, Tree

from mcc.exceptions import ParamMissingException
from mcc.languages import Lang


class Mccabe:
    suffixes: Tuple[str, ...]
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
        self.directory = directory
        self.file = file

    def _source_codes(self):
        if self.file:
            with open(self.file) as f:
                yield self.file, f.read()
        elif self.directory:
            for root, dirs, files in os.walk(self.directory):
                for file in files:
                    if not file.endswith(self.suffixes):
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

    def _complexity_item(self, args: Tuple[str, str]):
        file, code = args
        parser = Parser()
        parser.set_language(self.language.get_lib())
        tree = parser.parse(code.encode())  # type:Tree
        return file, self._visit_node(tree.root_node)

    def complexity(self):
        params = [(file, code) for file, code in self._source_codes()]
        with multiprocessing.Pool() as pool:
            return pool.map(self._complexity_item, params)

    def run(self):
        ret = {}
        for file, count in self.complexity():
            ret[file] = count
        return ret
