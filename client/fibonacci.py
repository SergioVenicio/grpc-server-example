from infra.grpc.pb import fibo_pb2, fibo_pb2_grpc

class Fibonacci:
  def __init__(self, stub: fibo_pb2_grpc.FibonacciStub) -> None:
    self.__stub = stub

  async def request_calc(self):
    number = int(input('Fibonacci: '))
    request = fibo_pb2.CalcRequest(number=number)
    response = self.__stub.CalcFibonacci.future(request).result()
    return {
      'id': response.processId,
      'status': response.status,
    }

  async def request_response(self):
    process_id = input('ProcessId: ')
    request = fibo_pb2.GetRequest(processId=process_id)
    response = self.__stub.GetFibonacci.future(request).result()
    return {
      'status': response.status,
      'result': response.result
    }