# Bài 10: Viết chương trình in ra tất cả các số nguyên tố nhỏ hơn 100.

for i in range(2,100):
    songuyento = 1
    for j in range(2,i):
        if i % j == 0:
            songuyento = 0
            break
    if songuyento == 1:
        print(i)
