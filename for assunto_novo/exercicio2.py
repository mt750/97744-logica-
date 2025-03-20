import os
import time

os.system("clear")

print("contagem de 100 ate 120 \nApenas pares: ")
for i in range(100,121):
    if i % 2 == 0:
        print(f"numero: {i} ")
        time.sleep(2)