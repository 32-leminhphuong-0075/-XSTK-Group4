# 1) Tìm giá trị trung bình và độ lệch chuẩn của X và Mốt của X;
# Tìm giá trị trung bình đồng thời là Mốt của X
n = 20
p = 0.4

expected_value = n * p
print(f"Giá trị trung bình của X (E(X)) = {expected_value:.2f}")

#Độ lệch chuẩn của
import math

standard_deviation = math.sqrt(n * p * (1 - p))
print(f"Độ lệch chuẩn của X (σ_X) = {standard_deviation:.2f}")

# 2) Tính (P(X = 10))
k = 10

probability_X_10 = math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
print(f"P(X = 10) = {probability_X_10:.6f}")
