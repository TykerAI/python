# Nhập vào số nguyên dương a, kiểm tra xem a có phải là số nguyên tố hay không 

a = int(input("Nhập vào số nguyên dương a: "))
so_nguyen_to = 1

if a <= 1:
    print(f"Vậy {a} không phải là số nguyên tố !!!")
else:
    for i in range(2,a):
        if a % i == 0:
            so_nguyen_to = 0
            break
    if so_nguyen_to == 1:
        print(f"Vậy {a} là số nguyên tố")
    else:
        print(f"Vậy {a} không phải là số nguyên tố !!!")




