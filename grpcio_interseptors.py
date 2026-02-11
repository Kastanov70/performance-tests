import grpc
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from contracts.services.gateway.users.rpc_get_user_pb2 import GetUserRequest


class SimpleLoggingInterceptor(grpc.UnaryUnaryClientInterceptor):
    def intercept_unary_unary(self, continuation, client_call_details, request):
        # Печатаем имя вызываемого метода
        print(f"[gRPC Interceptor] Calling method: {client_call_details.method}")
        
        # Выполняем реальный RPC вызов
        response = continuation(client_call_details, request)
        
        return response


interceptors = [SimpleLoggingInterceptor()]
channel = grpc.insecure_channel("localhost:9003")
intercept_channel = grpc.intercept_channel(channel, *interceptors)
stub = UsersGatewayServiceStub(channel=intercept_channel)

request = GetUserRequest(id="303c3019-a468-47bf-b06d-58dbb42babbc")
response = stub.GetUser(request)
print(response)
