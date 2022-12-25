# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import fibo_pb2 as fibo__pb2


class FibonacciStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CalcFibonacci = channel.unary_unary(
                '/Fibonacci/CalcFibonacci',
                request_serializer=fibo__pb2.CalcRequest.SerializeToString,
                response_deserializer=fibo__pb2.CalcResponse.FromString,
                )
        self.GetFibonacci = channel.unary_unary(
                '/Fibonacci/GetFibonacci',
                request_serializer=fibo__pb2.GetRequest.SerializeToString,
                response_deserializer=fibo__pb2.GetResponse.FromString,
                )


class FibonacciServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CalcFibonacci(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFibonacci(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FibonacciServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CalcFibonacci': grpc.unary_unary_rpc_method_handler(
                    servicer.CalcFibonacci,
                    request_deserializer=fibo__pb2.CalcRequest.FromString,
                    response_serializer=fibo__pb2.CalcResponse.SerializeToString,
            ),
            'GetFibonacci': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFibonacci,
                    request_deserializer=fibo__pb2.GetRequest.FromString,
                    response_serializer=fibo__pb2.GetResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Fibonacci', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Fibonacci(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CalcFibonacci(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Fibonacci/CalcFibonacci',
            fibo__pb2.CalcRequest.SerializeToString,
            fibo__pb2.CalcResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFibonacci(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Fibonacci/GetFibonacci',
            fibo__pb2.GetRequest.SerializeToString,
            fibo__pb2.GetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)