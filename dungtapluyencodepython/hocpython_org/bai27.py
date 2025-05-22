# Viết chương trình in ra hình tam giác rỗng có độ cao h được nhập từ bàn phím

h = int(input("Nhập vào chiều cao h: "))

for i in range(1, h + 1):
    if i == h:
        print("*" * (2*i-1))
    else:
        khoang_trong_dau = " " * (h-i)
        if i == 1:
            print(khoang_trong_dau + "*")
        else:
            khoang_trong_giua = " " * (2*i-3)
            print(khoang_trong_dau + "*" + khoang_trong_giua + "*")



