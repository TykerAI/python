# Nhập vào A, tìm n nhỏ nhất sao cho

# 1 + 1/2 + 1/3 + 1/4 + ... + 1/n > A

a = int(input("Nhập vào số nguyên dương a: "))

while a <= 0:
    print("Không phải số nguyên dương a, vui lòng nhập lại!!!")
    a = int(input("Nhập vào số nguyên dương a: "))

n = 0
tong = 0

while tong <= a:
    n += 1
    tong += 1/n
print(f"Vậy n = {n} là số nhỏ nhất sao cho n < A")


