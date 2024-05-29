xác_suất_x = [1/6, 2/6, 3/6]
xác_suất_y = [2/6, 3/6, 1/6]
# Tạo bảng phân phối xác suất chung của cặp biến (X, Y)
bảng_phân_phối = [[xác_suất_x[i] * xác_suất_y[j] for j in range(len(xác_suất_y))] for i in range(len(xác_suất_x))]

print("Bảng phân phối của cặp biến (X, Y):")
for hàng in bảng_phân_phối:
    print(hàng)

# Kiểm tra tính độc lập của X và Y
# Kiểm tra mỗi phần tử trong bảng phân phối xem có bằng 1/36 không (do 1/6 * 1/6 = 1/36)
độc_lập = all(abs(bảng_phân_phối[i][j] - 1/36) < 1e-9 for i in range(len(xác_suất_x)) for j in range(len(xác_suất_y)))

if độc_lập:
    print("X và Y là độc lập.")
#Nếu tất cả các giá trị trong bảng_phân_phối đều bằng 1/36 x y sẽ độc lập
else:
    print("X và Y không độc lập.")
#Nếu tất cả các giá trị trong bảng_phân_phối có giá trị không bằng 1/36 x y sẽ ko độc lập 
