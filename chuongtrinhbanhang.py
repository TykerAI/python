def tong_so_bill_KH(a, b):
	return a * b

def so_tien_thua_KH(a, b):
	so_tien_thua_return = b - a 
	if so_tien_thua_return >= 0 :
		return so_tien_thua_return
	else:
		return -1

def count_tien_thua(sotienthua):
	count_500 = int(sotienthua/500)
	sotienthua = sotienthua - 500*count_500
	if count_500 != 0:
		print("500k(VNĐ):", count_500 , "tờ")

	count_200 = int(sotienthua/200)
	sotienthua = sotienthua - 200*count_200
	if count_200 != 0:
		print("200k(VNĐ):", count_200 , "tờ")

	count_100 = int(sotienthua/100)
	sotienthua = sotienthua - 100*count_100
	if count_100 != 0:
		print("100k(VNĐ):", count_100 , "tờ")

	count_50 = int(sotienthua/50)
	sotienthua = sotienthua - 50*count_50
	if count_50 != 0:
		print("50k(VNĐ):", count_50 , "tờ")

	count_20 = int(sotienthua/20)
	sotienthua = sotienthua - 20*count_20
	if count_20 != 0:
		print("20k(VNĐ):", count_20 , "tờ")

	count_10 = int(sotienthua/10)
	sotienthua = sotienthua - 10*count_10
	if count_10 != 0:
		print("10k(VNĐ):", count_10 , "tờ")

	count_5 = int(sotienthua/5)
	sotienthua = sotienthua - 5*count_5
	if count_5 != 0:
		print("5k(VNĐ):", count_5 , "tờ")

	count_2 = int(sotienthua/2)
	sotienthua = sotienthua - 2*count_2
	if count_2 != 0:
		print("2k(VNĐ):", count_2 , "tờ")

	count_1 = int(sotienthua)
	if count_1 != 0:
		print("1k(VNĐ):", count_1 , "tờ")
	

def main():
	SO_TIEN_1KG_TAO = 21 #VNĐ
	so_weight_tao = input("Nhập số cân nặng của táo(kg): ")
	print("Số cân nặng của Táo là:" , so_weight_tao , "kg Táo")

	so_weight_tao = float(so_weight_tao) 
	total_bill = tong_so_bill_KH(SO_TIEN_1KG_TAO, so_weight_tao)
	print("===> Tổng bill của Khách Hàng là:", total_bill, "k VNĐ" )

	so_tien_KH_given = input("Nhập số tiền của Khách Hàng đưa cho bạn(k VNĐ): ")
	so_tien_KH_given = float(so_tien_KH_given)
	print("Số tiền Khách Hàng đưa cho bạn là:", so_tien_KH_given,"k VNĐ")

	total_sotienthua = so_tien_thua_KH(total_bill, so_tien_KH_given )
	if total_sotienthua == -1 :
		print("===> Số tiền Khách Hàng đưa bị thiếu", total_bill - so_tien_KH_given , "k VNĐ")
	else:
		print("===> Số tiền Khách Hàng đã đủ và còn dư:",total_sotienthua, "k VNĐ")
		print("===> Số tiền dư của Khách Hàng cần phải thối là:")
		count_tien_thua( total_sotienthua)



main()


