import grpc
import greet_pb2
import greet_pb2_grpc
import json
import asyncio

class reply:
  b : 'bbb'
  pass

def run():
    with grpc.insecure_channel('localhost:5000') as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        print("----output----")
       
        
        greet_pb2.HelloReply =  stub.SayHello(greet_pb2.HelloRequest(name='wenming')) 
        print(greet_pb2.HelloReply)

if __name__ == '__main__':
    run()
