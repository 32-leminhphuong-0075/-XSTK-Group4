def f(x):
    if 0 <= x <= 1:
        return 3 * x**2
    else:
        return 0

# Tính kỳ vọng
E_X = 0
for x in range(10000):
    x_i = x / 10000
    E_X += x_i * f(x_i)
E_X *= 1 / 10000
print("Kỳ vọng:", E_X) 
# Tính toán kỳ vọng:
#Sử dụng vòng lặp for để tính toán tích phân theo phương pháp Riemann.
#Chia nhỏ khoảng tích phân [0, 1] thành 10000 khoảng con có độ rộng bằng nhau.
#Tính toán giá trị f(x) tại mỗi điểm chia nhỏ.
#Cộng dồn các tích f(x) * độ rộng để tính toán tích phân.
#Chia kết quả cho 10000 để lấy giá trị trung bình.
# Tính phương sai
Var_X = 0
for x in range(10000):
    x_i = x / 10000
    Var_X += (x_i - E_X)**2 * f(x_i)
Var_X *= 1 / 10000
print("Phương sai:", Var_X)
#Tính toán phương sai:
#Sử dụng vòng lặp for để tính toán tích phân theo phương pháp Riemann.
#Chia nhỏ khoảng tích phân [0, 1] thành 10000 khoảng con có độ rộng bằng nhau.
#Tính toán giá trị (x - E_X)^2 * f(x) tại mỗi điểm chia nhỏ, trong đó E_X là kỳ vọng đã tính toán trước đó.
#Nhân giá trị (x - E_X)^2 * f(x) với độ rộng của khoảng con tương ứng.
#Cộng dồn các tích (x - E_X)^2 * f(x) * độ rộng để tính toán tích phân.
#Chia kết quả cho 10000 để lấy giá trị trung bình.

# Tính trung vị
def F(x):
    if 0 <= x <= 1:
        return 1.5 * x**3
    else:
        return 0

x_median = 0
for x in range(10000):
    x_i = x / 10000
    if F(x_i) >= 0.5:
        x_median = x_i
        break
print("Trung vị:", x_median)
#Tính toán trung vị:
#Định nghĩa hàm F(x) là tích phân của f(x) từ 0 đến x.
#Sử dụng vòng lặp for để tìm giá trị x sao cho F(x) = 0.5.
#Giá trị x tìm được chính là trung vị của biến ngẫu nhiên X.

# Tính hệ số bất đối xứng
Mu3 = 0
for x in range(10000):
    x_i = x / 10000
    Mu3 += (x_i - E_X)**3 * f(x_i)
Mu3 *= 1 / (Var_X**(3/2))
print("Hệ số bất đối xứng:", Mu3)
#Tính toán hệ số bất đối xứng:
#Sử dụng vòng lặp for để tính toán tích phân theo phương pháp Riemann.
#Chia nhỏ khoảng tích phân [0, 1] thành 10000 khoảng con có độ rộng bằng nhau.
#Tính toán giá trị (x - E_X)^3 * f(x) tại mỗi điểm chia nhỏ.
#Nhân giá trị (x - E_X)^3 * f(x) với độ rộng của khoảng con tương ứng.
#Cộng dồn các tích (x - E_X)^3 * f(x) * độ rộng để tính toán tích phân.
#Chia kết quả cho (Var_X)^(3/2), trong đó Var_X là phương sai đã tính toán trước đó.

# Tính hệ số nhọn
Mu4 = 0
for x in range(10000):
    x_i = x / 10000
    Mu4 += (x_i - E_X)**4 * f(x_i)
Mu4 *= 1 / (Var_X**2)
Mu4 -= 3
print("Hệ số nhọn:", Mu4)
#Tính toán hệ số nhọn:
#Sử dụng vòng lặp for để tính toán tích phân theo phương pháp Riemann.
#Chia nhỏ khoảng tích phân [0, 1] thành 10000 khoảng con có độ rộng bằng nhau.
#Tính toán giá trị (x - E_X)^4 * f(x) tại mỗi điểm chia nhỏ.
#Nhân giá trị (x - E_X)^4 * f(x) với độ rộng của khoảng con tương ứng.
#Cộng dồn các tích (x - E_X)^4 * f(x) * độ rộng để tính toán tích phân.
#Chia kết quả cho (Var_X)^2, trong đó Var_X là phương sai đã tính toán trước đó.
#Trừ 3 để lấy giá trị hệ số nhọn.

