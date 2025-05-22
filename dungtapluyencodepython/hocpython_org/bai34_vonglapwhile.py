# Nhập vào số nguyên dương a, nếu nhập số âm thì yêu cầu nhập lại cho đến khi người dùng nhập đúng số dương .
#Nếu người dùng nhập đúng số dương thì in ra “Bạn nhập đúng quy tắc”


a  = int(input("Nhập vào số nguyên dương a: "))

while a <= 0:
    print("Vui lòng nhập lại số nguyên dương a !!!")
    a = int(input("Nhập vào số nguyên dương a: "))
print("Đúng chuẩn quy tắc")
