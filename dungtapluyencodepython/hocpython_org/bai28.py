# Nhập vào n. Tính S = 1 + 2 + 3 + 4 + … + n

try:
    n = int(input("Nhập vào n: "))
    total = 0

    if n >= 0:
        for i in range(1,n+1):
            total += i
        print(f"Vậy S = {total}")
    else:
        print("Vui lòng nhập số nguyên dương !!!")
except:
    print("Vui lòng nhập số nguyên dương !!!")
