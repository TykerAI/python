# Từ bài số 15, nếu a, b, c cấu tạo thành được một tam giác, kiểm tra xem đó là tam giác gì (tam giác đều, tam giác vuông cân, tam giác vuông, tam giác cân hay tam giác thường)

a = int(input("Nhập vào độ dài cạnh a: "))
b = int(input("Nhập vào độ dài cạnh b: "))
c = int(input("Nhập vào độ dài cạnh c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Đây là tam giác đều")
    elif a == b or b == c or  a == c:
        print("Đây là tam giác cân")
    elif round(a**2 + b**2, 2) == round (c**2,2) or \
            round(b**2 + c**2, 2) == round(a**2,2) or \
            round(a**2 + c**2, 2) == round(b**2,2):
                if a == b or b == c or a == c:
                    print("Đây là tam giác vuông cân")
                    break
                else:
                    print("Đây là tam giác vuông")
                    break
    else:
        print("Đây là tam giác thường")


                

