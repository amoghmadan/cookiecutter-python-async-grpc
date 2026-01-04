from {{cookiecutter.project_name}}.core.management.commands.build import build
from {{cookiecutter.project_name}}.core.management.commands.loaddata import loaddata
from {{cookiecutter.project_name}}.core.management.commands.runserver import runserver
from {{cookiecutter.project_name}}.core.management.commands.shell import shell

commands = [build, loaddata, runserver, shell]

__all__ = ["commands"]
