# Giải và biện luận phương trình ax^2 + bx + c = 0

import math

a = int(input("Nhập vào hệ số a: "))
b = int(input("Nhập vào hệ số b: "))
c = int(input("Nhập vào hệ số c: "))

if a != 0:
    delta = b**2 -(4*a*c)
    if delta == 0:
        x = -b/(2*a)
        x = round(x, 2)
        print(f"Vậy phương trình đã cho có nghiệm kép x1 = x2 = {x}")
    elif delta > 0:
        x1 = -b - math.sqrt(delta) / (2*a)
        x1 = round(x1, 2)
        x2 = -b + math.sqrt(delta) / (2*a)
        x2 = round(x2, 2)
        print(f"Vậy phương trình {a}x^2 + {b}x + {c} = 0 có 2 nghiệm phân biệt x1 = {x1}, x2 = {x2}")
    else:
        print(f"Vậy phương trình {a}x^2 + {b}x + {c} = 0 vô nghiệm")
else:
    print("Đây là phương trình bậc nhất")
    

