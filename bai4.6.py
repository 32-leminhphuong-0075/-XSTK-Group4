#1:
# Bảng phân phối xác suất đồng thời của (X, Y)
phân_phối_xác_suất = [
    [0.10, 0.05, 0.15],
    [0.05, 0.15, 0.10],
    [0.10, 0.20, 0.10]
]

#2:
# Tính xác suất biên của X
xác_suất_X = [sum(hàng) for hàng in phân_phối_xác_suất]

# Tính xác suất biên của Y
xác_suất_Y = [sum(phân_phối_xác_suất[i][j] for i in range(len(phân_phối_xác_suất))) for j in range(len(phân_phối_xác_suất[0]))]

print("Phân phối xác suất biên của X:")
for i, p in enumerate(xác_suất_X, start=6):
    print(f"P(X={i}) = {p:.2f}")

print("\nPhân phối xác suất biên của Y:")
for j, p in enumerate(xác_suất_Y, start=1):
    print(f"P(Y={j}) = {p:.2f}")

# Tính Kỳ vọng của X và Y
giá_trị_X = [6, 7, 8]
giá_trị_Y = [1, 2, 3]

Kỳ_vọng_X = sum(giá_trị_X[i] * xác_suất_X[i] for i in range(len(giá_trị_X)))
Kỳ_vọng_Y = sum(giá_trị_Y[j] * xác_suất_Y[j] for j in range(len(giá_trị_Y)))

# Tính Kỳ vọng của X^2 và Y^2
Kỳ_vọng_X2 = sum(giá_trị_X[i]**2 * xác_suất_X[i] for i in range(len(giá_trị_X)))
Kỳ_vọng_Y2 = sum(giá_trị_Y[j]**2 * xác_suất_Y[j] for j in range(len(giá_trị_Y)))

# Tính Phương sai của X và Y
Phương_sai_X = Kỳ_vọng_X2 - Kỳ_vọng_X**2
Phương_sai_Y = Kỳ_vọng_Y2 - Kỳ_vọng_Y**2

print(f"\nKỳ vọng của X = {Kỳ_vọng_X:.2f}")
print(f"Kỳ vọng của Y = {Kỳ_vọng_Y:.2f}")
print(f"Phương sai của X = {Phương_sai_X:.2f}")
print(f"Phương sai của Y = {Phương_sai_Y:.2f}")

#3:
# Bảng phân phối xác suất của Y với điều kiện X = 7
xác_suất_điều_kiện_Y_khi_X_bằng_7 = [phân_phối_xác_suất[1][j] / xác_suất_X[1] for j in range(len(phân_phối_xác_suất[0]))]

print("\nBảng phân phối xác suất của Y với điều kiện X = 7:")
for j, p in enumerate(xác_suất_điều_kiện_Y_khi_X_bằng_7, start=1):
    print(f"P(Y={j} | X=7) = {p:.2f}")

#4:
# Tính P(X = 6)
P_X_6 = xác_suất_X[0]

# Tính P(X ≥ 7, Y ≥ 2)
P_X_lớn_hơn_bằng_7_Y_lớn_hơn_bằng_2 = sum(phân_phối_xác_suất[i][j] for i in range(1, 3) for j in range(1, 3))

print(f"\nP(X=6) = {P_X_6:.2f}")
print(f"P(X ≥ 7, Y ≥ 2) = {P_X_lớn_hơn_bằng_7_Y_lớn_hơn_bằng_2:.2f}")
