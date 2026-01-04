from grpc.aio import ServerInterceptor

from {{cookiecutter.project_name}}.interceptors.logging import AsyncLoggingInterceptor

interceptors: list[ServerInterceptor] = [AsyncLoggingInterceptor()]

__all__ = ["interceptors"]
