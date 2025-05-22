# Nhập vào 3 số thực dương a, b, c. Kiểm tra xem a, b, c có cấu thành độ dài của 1 tam giác được không

a = int(input("Nhập vào số thực dương a: "))
b = int(input("Nhập vào số thực dương b: "))
c = int(input("Nhập vào số thực dương c: "))

if a + b > c and a + c > b and b + c > a:
    print("Vậy 3 cạnh a, b, c cấu thành độ dài của tam giác ABC")
else:
    print("Vậy 3 cạnh a, b, c không cấu thành độ dài của tam giác ABC")
