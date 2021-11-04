import click

from CyclomaticComplexity import get_provider_class
from CyclomaticComplexity.languages import Lang
from CyclomaticComplexity.version import VERSION


@click.command()
@click.version_option(VERSION, "-V", "--version")
@click.option("-d", "--directory", required=False, help="The source code directory")
@click.option("-f", "--file", required=False, help="The source code file")
@click.option("-s", "--source", required=False, help="The raw source code")
@click.option(
    "-l",
    "--language",
    type=click.Choice([lang for lang in Lang], case_sensitive=False),
    required=True,
    help="The source code language",
)
def cli(directory: str, file: str, source: str, language: Lang):
    if not any([directory, file, source]):
        raise click.UsageError(
            "You must specify a source code file or directory or raw source code"
        )
    get_provider_class(language)(directory, file, source).run()


def main():
    cli()


if __name__ == "__main__":
    main()
