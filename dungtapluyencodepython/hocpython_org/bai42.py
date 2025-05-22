# Dãy số fibonacci là dãy số được định nghĩa như sau: 1, 1, 2, 3, 5, 8, 13,... với số kế tiếp sẽ bằng tổng hai số trước đó

# Nhập vào A, hãy tìm số trong dãy số fibonacci lớn nhất nhưng không vượt quá A 

A = int(input("Nhập vào A: "))
while A <= 0:
    A = int(input("Nhập vào A: "))

a1 = 1
a2 = 1
a_tong = 1

while True:
    a_ketiep = a1 + a2
    if a_ketiep > A:
        break
    a_tong = a_ketiep
    a1 = a2
    a2 = a_ketiep
print(f"Vậy số kế tiếp không vượt quá a là: {a_tong}")

