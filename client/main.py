import asyncio
import grpc

from infra.grpc.pb.fibo_pb2_grpc import FibonacciStub

from fibonacci import Fibonacci


async def request_calc(channel):
  fibonacci = Fibonacci(FibonacciStub(channel))
  try:
    response = await fibonacci.request_calc()
    print(response)
  except ValueError:
    print('invalid number')


async def request_response(channel):
  fibonacci = Fibonacci(FibonacciStub(channel))
  response = await fibonacci.request_response()
  print(response)
  

def show_menu():
  print('1 - GET RESPONSE')
  print('2 - REQUEST CALC')


async def main(channel):  
  valid_choices = {
    '1': request_response,
    '2': request_calc
  }

  while True:
    show_menu()
    option = input('Option #: ')
    if option not in valid_choices.keys():
      print('invalid')
      return

    await valid_choices.get(option)(channel)


async def run():
  with grpc.insecure_channel('localhost:50051') as channel:
    await main(channel)


if __name__ == '__main__':
  asyncio.run(run())