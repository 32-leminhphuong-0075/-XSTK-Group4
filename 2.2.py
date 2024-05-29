# a)
#bảng phân phối xác suất của X
p1 = 0.7
p2 = 0.8
# b)
#xác suất để số viên đạn trúng thú của hai người bằng nhau
P_X0 = (1-p1)*(1-p2)
P_X1 = p1*(1-p2) + (1-p1)*p2
P_X2 = p1*p2

P_equal = P_X1 * P_X1

print("Xác suất của X = 0: ", P_X0)
print("Xác suất của X = 1: ", P_X1)
print("Xác suất của X = 2: ", P_X2)
print("Xác suất để số viên đạn trúng của hai người bằng nhau: ", P_equal)

