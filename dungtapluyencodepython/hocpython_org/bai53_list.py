# Nhập vào một list số nguyên L, tìm và in ra giá trị lớn nhất trong L 
L = list(map(int, input("Nhập vào một list số nguyên L:").split()))

L_max = 0
for i in L:
    if i >= L_max:
        L_max = i
print(f"Vậy giá trị lớn nhất trong L: {L_max}")

