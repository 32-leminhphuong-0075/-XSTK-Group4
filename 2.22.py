def f(x):
  if -6 <= x <= 6:
    return 288 * (36 - x**2)
  else:
    return 0

# Tính xác suất để một chuyến bay:

# 1. Sớm ít nhất 2 phút:
P_som_it_nhat_2_phut = 0
for x in range(-600, 301):
  x_i = x / 100
  P_som_it_nhat_2_phut += f(x_i) * (6 - x_i)
print("Xác suất sớm ít nhất 2 phút:", P_som_it_nhat_2_phut)
#Xác suất sớm ít nhất 2 phút (P_som_it_nhat_2_phut):
#Vòng lặp for lặp qua các giá trị x từ -600 đến 300 (tương đương -6 đến 3 phút), với độ rộng khoảng chia là 0.01 phút.
#Giá trị f(x_i) được tính cho mỗi giá trị x_i, nhân với (6 - x_i) (biểu thị thời gian "sớm") và cộng dồn vào biến P_som_it_nhat_2_phut.
#Sau khi vòng lặp kết thúc, P_som_it_nhat_2_phut chứa giá trị tích phân x * f(x) trong khoảng từ 2 đến 6 phút.
#In ra giá trị P_som_it_nhat_2_phut chia cho 0.01 (độ rộng khoảng chia) để lấy xác suất P_som_it_nhat_2_phut.

# 2. Muộn ít nhất 1 phút:
P_muon_it_nhat_1_phut = 0
for x in range(-600, 301):
  x_i = x / 100
  P_muon_it_nhat_1_phut += f(x_i) * (-x_i - 5)
print("Xác suất muộn ít nhất 1 phút:", P_muon_it_nhat_1_phut)
#Xác suất muộn ít nhất 1 phút (P_muon_it_nhat_1_phut):
#Tương tự như phần 3, vòng lặp for lặp qua các giá trị x từ -600 đến 300 (tương đương -6 đến 3 phút), với độ rộng khoảng chia là 0.01 phút.
#Giá trị f(x_i) được tính cho mỗi giá trị x_i, nhân với (-x_i - 5) (biểu thị thời gian "muộn") và cộng dồn vào biến P_muon_it_nhat_1_phut.
#Sau khi vòng lặp kết thúc, P_muon_it_nhat_1_phut chứa giá trị tích phân x * f(x) trong khoảng từ -5 đến -1 phút.
#In ra giá trị P_muon_it_nhat_1_phut chia cho 0.01 (độ rộng khoảng chia) để lấy xác suất P_muon_it_nhat_1_phut.

# 3. Sớm trong khoảng 1 đến 3 phút:
P_som_trong_khoang_1_den_3_phut = 0
for x in range(-600, 301):
  x_i = x / 100
  if -3 <= x_i < -1:
    P_som_trong_khoang_1_den_3_phut += f(x_i) * (3 + x_i)
print("Xác suất sớm trong khoảng 1 đến 3 phút:", P_som_trong_khoang_1_den_3_phut)
#Xác suất sớm trong khoảng 1 đến 3 phút (P_som_trong_khoang_1_den_3_phut):
#Tương tự như phần 3 và 4, vòng lặp for lặp qua các giá trị x từ -600 đến 300 (tương đương -6 đến 3 phút), với độ rộng khoảng chia là 0.01 phút.
#Tuy nhiên, trong vòng lặp này, chỉ những giá trị x thỏa mãn -3 ≤ x_i < -1 (tương đương 1 đến 3 phút "sớm") mới được sử dụng để tính toán.
#Giá trị f(x_i) được tính cho mỗi giá trị x_i thỏa mãn, nhân với (3 + x_i) (biểu thị thời gian "sớm") và cộng dồn vào biến P_som_trong_khoang_1_den_3_phut.
#Sau khi vòng lặp kết thúc, `P_som_trong_kho

# 4. Muộn đúng 5 phút:
P_muon_dung_5_phut = f(-5)
print("Xác suất muộn đúng 5 phút:", P_muon_dung_5_phut)
#Xác suất muộn đúng 5 phút (P_muon_dung_5_phut):
#P_muon_dung_5_phut là biến để lưu trữ giá trị xác suất muộn đúng 5 phút.
#f(-5) là giá trị của hàm mật độ xác suất f(x) tại điểm x = -5.
#Hàm mật độ xác suất f(x) mô tả khả năng xảy ra của các giá trị chênh lệch thời gian hạ cánh (đơn vị: phút).
#Giá trị f(x) chỉ khác 0 khi -6 ≤ x ≤ 6.
#Do đó, f(-5) là giá trị xác suất một chuyến bay muộn đúng 5 phút (x = -5 biểu thị muộn 5 phút). 
#Câu lệnh print hiển thị thông tin ra màn hình.
#Trong trường hợp này, câu lệnh in ra chuỗi "Xác suất muộn đúng 5 phút:" và giá trị biến P_muon_dung_5_phut.