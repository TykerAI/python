# Nhập vào một chuỗi, hãy đếm xem trong chuỗi có bao nhiêu từ (quy định là chuỗi không có ký tự đặc biệt, không số, không có dấu câu, chỉ có ký tự chữ và khoảng trắng)

chuoi = input("Nhập vào một chuỗi: ").strip()

# Tách chuỗi thành danh sách các từ
tu_list = chuoi.split()

# Đếm số từ
so_tu = len(tu_list)

print(f"Số lượng từ trong chuỗi là: {so_tu}")

