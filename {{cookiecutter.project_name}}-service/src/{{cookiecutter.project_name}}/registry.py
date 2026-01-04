from {{cookiecutter.project_name}}.protobuf.healthcheck import healthcheck_pb2_grpc
from {{cookiecutter.project_name}}.services import HealthCheckService

register = {
    HealthCheckService: healthcheck_pb2_grpc.add_HealthCheckServiceServicer_to_server,
}
