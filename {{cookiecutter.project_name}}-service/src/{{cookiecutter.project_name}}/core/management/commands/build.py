import sys
from pathlib import Path

import click
from grpc_tools.protoc import _get_resource_file_name, main

from {{cookiecutter.project_name}}.conf import settings


@click.command()
@click.option(
    "-o",
    "--out-dir",
    default="src",
    type=click.Path(),
    help="Output directory for protobuf.",
)
@click.pass_context
def build(ctx: click.Context, out_dir: str) -> None:
    """Build gRPC code from .proto files."""
    project_root = settings.BASE_DIR.parent  # type: ignore[attr-defined]
    if Path.cwd() != project_root:
        raise click.ClickException("Run this command from the project's root.")
    arguments = [
        _get_resource_file_name("grpc_tools", "protoc.py"),
        "-I./proto",
        f"--python_out={out_dir}",
        f"--grpc_python_out={out_dir}",
        *(
            str(path.relative_to(project_root))
            for path in (project_root / "proto").glob("**/*.proto")
        ),
        f"-I{_get_resource_file_name("grpc_tools", "_proto")}",
    ]
    protoc = main(arguments)
    if protoc:
        sys.exit(protoc)
    for path in Path(out_dir).resolve().rglob("**/*/"):
        if path.is_dir() and ".egg-info" not in str(path):
            (path / "__init__.py").touch(exist_ok=True)
    sys.exit(protoc)
