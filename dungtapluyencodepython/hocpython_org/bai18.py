# Giải và biện luận phương trình ax + b = 0

a = float(input("Nhập vào số nguyên a: "))
b = float(input("Nhập vào số nguyên b: "))

if a == 0:
    if b == 0:
        print("Phương trình {a}x + {b} = 0 có vô số nghiệm")
    else:
        print("Phương trình {a}x + {b} = 0 vô nghiệm")
else:
    x = -b/a
    print(f"Phương trình {a}x + {b} = 0 có nghiệm  x = {x}")
