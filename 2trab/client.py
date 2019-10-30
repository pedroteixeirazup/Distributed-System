import grpc

import calculator_pb2
import calculator_pb2_grpc
import calculator

channel = grpc.insecure_channel('localhost:50051')

stub = calculator_pb2_grpc.CalculatorStub(channel)

# number = calculator_pb2.Number(value = 16)
print('Digite a posicao e o valor')
pos = input()
x = input()
string = calculator_pb2.String(pos = pos, value = x)

# response = stub.SquareRoot(number)
response_s = stub.PutInString(string)

def mount_tabu():
    print(calculator.recuper_tabu(calculator.mount_tabu()))


with open('data.txt','a+') as f:
    data=str(response_s.value)
    f.write(data)

print(response_s.value)

mount_tabu()