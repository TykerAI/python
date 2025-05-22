# Nhập vào một số nguyên dương n, kiểm tra xem n có phải là số dạng 2^k hay không 

n = int(input("Nhập vào số nguyên dương n: "))
while n <= 0:
    n = int(input("Nhập vào số nguyên dương n: "))

a = n
while a % 2 == 0:
    a = a // 2

if a == 1:
    print(f"Vậy {n} là số dạng 2^k")
else:
    print(f"Vậy {n} không phải là số dạng 2^k")
