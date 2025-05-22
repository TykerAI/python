# Nhập n. Cho S(k) = 1 + 2 + 3 + … + k. Tìm k sao cho S(k) lớn nhất nhưng nhỏ hơn n

n = int(input("Nhập vào số nguyên dương n: "))

while n <= 0:
    print("Vui lòng nhập n là số nguyên dương. Nhập lại !!!")
    n = int(input("Nhập vào số nguyên dương n: "))

k = 0
tong = 0 

while True:
    k += 1
    tong += k
    if tong >= n:
        k -= 1
        break

