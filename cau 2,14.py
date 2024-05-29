def f(x):
    if 10 < x < 20:
        return 1
    else:
        return 0

# Tính tổng xác suất trên khoảng (10, 20)
total_probability = sum(f(x) for x in range(11, 20))
print("Tổng xác suất trên khoảng (10, 20):", total_probability)

# Kiểm tra xác suất không âm
is_non_negative = all(f(x) >= 0 for x in range(11, 20))
print("Xác suất không âm:", is_non_negative)

# kiểm tra f(x) có phải là hàm mật độ xác xuất 
if  is_non_negative == True:
    print("f(x) là hàm mật độ xác xuất")
else:
    print("f(x) không phải là hàm mật độ xác xuất")
