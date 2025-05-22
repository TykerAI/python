# Nhập vào 3 số a, b, c. Tính và in ra d = (a + b)^c
# Nếu d là số trong khoảng từ 100 - 200 thì in ra True, ngược lại in ra False 

import math

a = int(input("Nhập số nguyên a:"))
b = int(input("Nhập số nguyên b:"))
c = int(input("Nhập số nguyên c:"))

d = (a+b)**c
print(f"Vậy d = ({a} + {b}) ** {c} = {(a+b)**c}")

if 100 <= d <= 200:
    print("True")
else:
    print("False")
