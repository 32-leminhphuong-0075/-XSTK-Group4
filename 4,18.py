# Kích thước của không gian mẫu (hình vuông 60x60)
total_area = 60 * 60

# Diện tích các tam giác ngoài dải gặp nhau
# Tam giác vuông 1: (0, 0), (0, 15), (15, 0)
triangle1_area = 0.5 * 15 * 15

# Tam giác vuông 2: (45, 60), (60, 60), (60, 45)
triangle2_area = 0.5 * 15 * 15

# Tổng diện tích của hai tam giác ngoài dải
total_triangle_area = 2 * triangle1_area

# Diện tích dải thoả mãn điều kiện |X - Y| <= 15
successful_area = total_area - total_triangle_area

# Xác suất để họ gặp nhau
probability = successful_area / total_area

print(f"Xác suất để hai người bạn gặp nhau và cùng nhau đi chơi là: {probability:.4f}")