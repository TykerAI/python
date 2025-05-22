# Ngày vào ngày, tháng. Hãy tính và in ra xem ngày nhập vào cách ngày đầu năm bao nhiêu ngày (giả sư năm đó không phải là năm nhuận)


try:
    day = int(input("Nhập vào ngày hiện tại: "))
    month = int(input("Nhập vào tháng hiện tại: "))
    list_month = [31,28,31,30,31,30,31,31,30,31,30,31]

    if day < 1 and day > list_month[day-1]:
        print("Ngày bạn nhập không hợp lệ: ")
    elif month < 1 and month > 12:
        print("Tháng bạn nhập không hợp lệ")
    else:
        total = 0
        for i in range(month):
            total += list_month[month-1]
        total += day

    print(f"Vậy ngày {day}/{month} cách ngày 1/1 là {total} ngày ")
except:
    pass
    




