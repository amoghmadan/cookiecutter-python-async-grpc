import os
import subprocess

import click


@click.command()
@click.pass_context
def shell(ctx: click.Context) -> None:
    """Python shell with application context."""
    subprocess.call(["python", "-i"], env=os.environ)
