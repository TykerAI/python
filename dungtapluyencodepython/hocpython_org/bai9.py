# Nhập vào số nguyên a, kiểm tra xem a có phải là số chính phương hay không, nếu có thì in ra True, ngược lại in ra False

a = int(input("Nhập vào số nguyên a: "))

for i in range(a+1):
    sochinhphuong = 0
    if i*i == a:
        sochinhphuong = 1
        break
if sochinhphuong == 1:
    print(f"Vậy a = {a} là số chính phương")
else:
    print(f"Vậy a = {a} không phải là số chính phương" )
