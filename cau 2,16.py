import math

# Khai báo hàm mật độ xác suất
def pdf(x, theta):
    if x > 0:
        return (1 / theta) * math.exp(-x / theta)
    else:
        return 0

# Khai báo hàm phân phối xác suất
def cdf(x, theta):
    if x <= 0:
        return 0
    else:
        return 1 - math.exp(-x / theta)

# Tính P(0 < X < theta)
def prob_between_0_and_theta(theta):
    return cdf(theta, theta) - cdf(0, theta)

# Đặt giá trị theta
theta = 2.0

# In kết quả
print("Hệ số a:", 1 / theta)
print("P(0 < X < theta):", prob_between_0_and_theta(theta))