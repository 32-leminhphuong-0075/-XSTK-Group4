from itertools import combinations

# Số sản phẩm của mỗi loại
tong_A = 8
tong_B = 5
tong_C = 3

# Tổng số sản phẩm
tong_san_pham = tong_A + tong_B + tong_C

# Số sản phẩm được lấy ra
san_pham_lua_chon = 3

# Khởi tạo bảng phân phối xác suất đồng thời của (X, Y)
bang_xac_suat = {}

# Tạo tất cả các tổ hợp có thể của 3 sản phẩm được chọn từ 15 sản phẩm
cac_to_hop = list(combinations(range(tong_san_pham), san_pham_lua_chon))

# Đếm số lượng sản phẩm loại A và B trong từng tổ hợp
for to_hop in cac_to_hop:
    dem_A = sum(1 for i in to_hop if i < tong_A)
    dem_B = sum(1 for i in to_hop if tong_A <= i < tong_A + tong_B)
    
    # Tăng cộng số lượng tổ hợp vào bảng phân phối xác suất đồng thời
    bang_xac_suat[(dem_A, dem_B)] = bang_xac_suat.get((dem_A, dem_B), 0) + 1

# Tính xác suất cho mỗi cặp (X, Y)
tong_to_hop = len(cac_to_hop)
for key in bang_xac_suat:
    bang_xac_suat[key] /= tong_to_hop

# In bảng phân phối xác suất đồng thời
print("Bảng phân phối xác suất đồng thời (X, Y):")
print("X\tY\tP(X,Y)")
for key in bang_xac_suat:
    print(f"{key[0]}\t{key[1]}\t{bang_xac_suat[key]}")
