# Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số chẵn, bao nhiêu chữ số lẻ

n = int(input("Nhập vào số nguyên dương n: "))
while n <= 0:
    n = int(input("Không phải số nguyên dương, vui lòng nhập lại: "))

dem_so_chan = 0
dem_so_le = 0
while n != 0:
    a = n % 10
    n = n / 10
    if a % 2 == 0:
        dem_so_chan += 1
    else:
        dem_so_le += 1
print(f"Vậy n có {dem_so_chan} chữ số chẵn và có {dem_so_le} chữ số lẻ")

