def get_grpc_application():
    from {{cookiecutter.project_name}}.core.handlers.grpc import GRPCHandler

    return GRPCHandler()
