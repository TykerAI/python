# Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số

n = int(input("Nhập vào số nguyên dương n: "))
while n <= 0:
    n = int(input("Vui lòng nhập lại số nguyên dương n: "))

dem = 0
while True:
    dem += 1
    n = n // 10
    if n == 0:
        break
print(f"Có {dem} chữ số") 


