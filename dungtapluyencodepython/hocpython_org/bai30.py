# Nhập vào số nguyên dương a, đếm số ước của a 

try:
    a = int(input("Nhập vào số nguyên dương a: "))
    dem = 0

    if a >= 0:
        for i in range(1,a+1):
            if a % i == 0:
                dem += 1
        print(f"Vậy số ước của {a} là: {dem}")
    else:
        print("Vui lòng nhập số nguyên dương !!!")
except:
    print("Vui lòng nhập số nguyên dương !!!")
