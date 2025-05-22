# Nhập vào số nguyên dương a và b, in toàn bộ ước chung của a và b

a = int(input("Nhập vào số nguyên dương a: "))
b = int(input("Nhập vào số nguyên dương b: "))

ds_uoc_chung = []

for i in range(1, min(a,b)+1):
    if a % i == 0 and b % i == 0:
        ds_uoc_chung.append(i)
print(f"Vậy ước chung của {a} và {b} là: {ds_uoc_chung}")
