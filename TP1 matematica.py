from time import sleep

for num in range(16):
    n = num
    binario = ''
    
    if n == 0:
        binario = '0'
    else:
        while n > 0:
            binario = str( n % 2) + binario
            n = n // 2
    print(f"{num} en binario es {binario}")
    sleep(0.5)

for num in range(16):
    print(f"{num} en binario es {bin(num)[2:]}")
    sleep(0.5)