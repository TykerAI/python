try:
    diem = []
    mon = ["Toán", "Văn", "Anh"]
    for i in range(len(mon)):
        a = round(float(input(f"Nhập vào điểm môn {mon[i]}: ")))
        diem.append(a)

    if all(0 <= a <= 10 for a in diem):
        diemtb = sum(diem)/len(diem)
        if diemtb >= 8 and (diem[0] >= 8 or diem[1] >= 8) and \
                min(diem) >= 6.5:
                    print("Học sinh giỏi")
        elif diemtb >= 6.5 and (diem[0] >= 6.5 or diem[1] >= 6.5) and \
                min(diem) >= 5:
                    print("Học sinh khá")
        elif diemtb >= 5 and (diem[0] >= 5 or  diem[1] >= 5) and \
                min(diem) >= 3.5:
                    print("Học sinh trung bình")
        elif diemtb >= 3.5 and (diem[0] >= 3.5 or diem[1] >= 3.5) and \
                min(diem) >= 2:
                    print("Học sinh yếu")
        else:
            print("Học sinh kém")
    else:
        print("Vui lòng nhập điểm trong khoảng (0 - 10) !!!")
except:
    print("Vui lòng nhập điểm bằng số !!!")
