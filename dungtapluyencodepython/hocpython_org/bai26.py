# Nhập vào số nguyên dương a, in ra bảng cửu chương của a

try:
    a = int(input("Nhập vào số nguyên dương của a: "))

    if a > 0:
        print(f"----------Bảng cửu chương của {a}----------")
        for i in range(1, 11):
            print(f"{a} x {i} = {a * i}")
    else:
        print("Vui lòng nhập số nguyên dương a !!!")
except:
    print("Vui lòng nhập số nguyên dương a !!!")
