"""Console script for wk02_exersice."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for wk02_exersice."""
    click.echo("Replace this message by putting your code into "
               "wk02_exersice.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
