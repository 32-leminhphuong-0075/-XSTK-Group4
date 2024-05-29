# a)
#Bảng phân phối xác suất
P_0 = 0.1
P_5 = 0.3
P_10 = 0.6
P_15 = 0
# b)
#Kỳ vọng
E_X = 0*P_0 + 5*P_5 + 10*P_10 + 15*P_15
print("Kỳ vọng của X là :", E_X)
#Phương Sai
E_X2 = 0**2*P_0 + 5**2*P_5 + 10**2*P_10 + 15**2*P_15
var_X = E_X2 - E_X**2
print("Phương sai của X là :", var_X)
#Độ lệch chuẩn
std_dev_X = var_X**0.5
print("Độ lệch chuẩn X là :", std_dev_X)