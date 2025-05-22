# Bài 9: Viết chương trình kiểm tra xem một số có phải là số nguyên tố hay không.

a = int(input("Nhập vào một số bất kỳ: "))
songuyento = 1
for i in range(2,a):
    if a % i == 0:
        songuyento= 0
        break
if songuyento == 1:
    print(f"Vậy a = {a} là số nguyên tố")
else:
    print(f"Vậy a = {a} không phải là số nguyên tố")
