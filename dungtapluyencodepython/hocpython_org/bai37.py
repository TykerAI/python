# Nhập vào một dãy số nguyên, ngưng nhập khi người dùng nhập -1.

# Sau khi nhập xong, in số lớn nhất, số nhỏ nhất trong những số vừa nhập

day_so = []

while True:
    n = int(input("Nhập vào số nguyên dương n: "))
    if n == -1:
        break
    day_so.append(n)

if len(day_so) == 0:
    print("Không có phần tử nào cả !!!")
else:
    print(day_so)
    print(f"Vậy số lớn nhất trong những số vừa nhập là: {min(day_so)}")
    print(f"Vậy số bé nhất trong những số vừa nhập là: {max(day_so)}")
