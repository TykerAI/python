# Nhập vào số nguyên dương n, tính tổng các chữ số của n  
n = int(input("Nhập vào số nguyên dương n: "))
while n <= 0:
    n = int("Nhập vào số nguyên dương n: ")

a = 0
total = 0
while n != 0:
    a = n % 10
    total += a
    n = n // 10
print(f"Vậy tổng các chữ số của n là: {total}")

    

