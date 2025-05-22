# Nhập vào số nguyên dương a, in toàn bộ ước của a 

a = int(input("Nhập vào số nguyên dương của a: "))
list = []
for i in range(1, a+1):
    if a % i == 0:
        list.append(i)
print(f"Vậy ước của {a} là: {list}")

