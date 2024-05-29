#  | X |   0  |   1  |  2  |  3  |  4  |
#  | P | 0,05 | 0,15 | 0,4 | 0,3 |  p  |
# a)
tong = 0.05 + 0.15 + 0.4 + 0.3              # = 0.9
p = 1 - tong                                # = 0.1
# P = P(2) + P(3) + P(4)
P = 0.15 + 0.4 + 0.3 + 0.1                  # = 0.95
print("Giá trị của p là : ", p)
print("Xác suất của có số hợp đồng từ 2 trở lên là : ", P)

# b)
f_0 = 0.05
f_1 = 0.15
f_2 = 0.4
f_3 = 0.3
f_4 = 0.1
print("Hàm khối lượng xác suất thứ nhất là : ", f_0 )
print("Hàm khối lượng xác suất thứ hai là : ", f_1 )
print("Hàm khối lượng xác suất thứ ba là : ", f_2 )
print("Hàm khối lượng xác suất thứ tư là : ", f_3 )
print("Hàm khối lượng xác suất thứ năm là : ", f_4 )

# c)
# Kỳ vọng :
E_X = 0*0.05 + 1*0.15 + 2*0.4 + 3*0.3 + 4*0.1    
# Phương sai : 
# V(X) = [E(X^2)] - [E(X)]^2
E_1 = 0**2 * 0.05
E_2 = 1**2 * 0.15
E_3 = 2**2 * 0.4
E_4 = 3**2 * 0.3
E_5 = 4**2 * 0.1

E_6 = (E_X)**2

V_X = ( E_1 + E_2 + E_3 + E_4 + E_5) - E_6
print("Kỳ vọng là : ", E_X)
print("Phương sai là : ", V_X)

# d)
# LN = lợi nhuận
E_LN =  E_X * 100
V_LN =  V_X * 100**2
print("Kỳ vọng lợi nhuận nhận được là : ", E_LN , "triệu đồng")
print("Phương sai lợi nhuận nhận được là : ", V_LN , "triệu đồng")