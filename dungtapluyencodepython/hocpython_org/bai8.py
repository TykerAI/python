# Nhập vào số thực a, kiểm tra xem a có phải là số nguyên hay không, nếu có thì in ra True, ngược lại in ra False

a = float(input("Nhập vào số thực a: "))
# Hàm is_integer() là hàm có sẵn trong python kiểm tra xem có phải số nguyên hay không
if a.is_integer():
    print("True")
else:
    print("")
