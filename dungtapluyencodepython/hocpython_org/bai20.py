# Nhập tháng, năm. Hãy cho biết tháng đó có bao nhiêu ngày

try:
    CURRENT_YEAR = int(input("Nhập vào năm hiện tại: "))
    month  = int(input("Nhập tháng (1-12): "))

    if 1 <= month <= 12:
        if month in [1,3,5,7,8,10,12]:
            days = 31
        elif month == 2:
            if CURRENT_YEAR % 4 == 0:
                days = 29
            else:
                days = 28
        else:
            days = 30
        print(f"Vậy tháng {month} năm {CURRENT_YEAR} có {days} ngày.")
    else:
        print("Tháng bạn nhập không hợp lệ!!!")
except:
    print("Vui lòng nhập số!!!")
