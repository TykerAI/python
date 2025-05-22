# Nhập vào 3 số a, b, c. Hãy sắp xếp 3 số a, b, c theo thứ tự tăng dần rồi in ra lại

number = []

number.append(int(input("Nhập vào số nguyên a: ")))
number.append(int(input("Nhập vào số nguyên b: ")))
number.append(int(input("Nhập vào số nguyên c: ")))

for i in range (len(number)):
    for j in range(i+1,len(number)):
        if number[i] > number[j]:
            number[i], number[j] = number[j], number[i]
print(number)
