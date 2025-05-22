# Nhập vào lương tháng này nhận được, ta phải đưa cho vợ 90% số tiền lương đó. Hãy in ra lương ta giữ lại

money = int(input("Nhập vào số lương tháng này nhận được: "))
givemoneyforu = (money*90)/100
money = money - givemoneyforu
print(f"Số tiền lương còn lại: {money}VNĐ")
