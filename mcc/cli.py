import json
import sys

import click

from mcc import get_provider_class
from mcc.languages import Lang
from mcc.version import VERSION


@click.command(name="mcc", help="Calculate the cyclomatic complexity of the source code")
@click.version_option(VERSION, "-V", "--version")
@click.option("-d", "--directory", required=False, help="The source code directory")
@click.option("-f", "--file", required=False, help="The source code file")
@click.option("-m", "--min", "min_value", type=int, required=False, help="The min threshold value")
@click.option(
    "-l",
    "--language",
    type=click.Choice([lang for lang in Lang], case_sensitive=False),
    required=True,
    help="The source code language",
)
def cli(directory: str, file: str, language: Lang, min_value: int):
    if not any([directory, file]):
        raise click.UsageError(
            "You must specify a source code file or directory or raw source code"
        )
    ret = get_provider_class(language)(directory, file).run()
    if min_value:
        ret = {k: v for k, v in ret.items() if v > min_value}
    click.echo(json.dumps(ret, indent=4))


def main():
    sys.path.insert(0, ".")
    cli()


if __name__ == "__main__":
    main()
