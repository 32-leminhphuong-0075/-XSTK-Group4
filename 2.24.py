def tich_phan(f, a, b, n=1000):
    # Tích phân số sử dụng quy tắc hình thang
    h = (b - a) / n
    ket_qua = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        ket_qua += f(a + i * h)
    return ket_qua * h
#Định nghĩa hàm tich_phan(f, a, b, n):
#Hàm này sử dụng quy tắc hình thang để tính tích phân số f(x) trong khoảng từ a đến b.
#Tham số n là số lượng hình thang được sử dụng để xấp xỉ diện tích dưới đồ thị hàm số.
#Hàm trả về giá trị tích phân.

# Định nghĩa hàm mật độ xác suất từng đoạn
def f(x, a):
    if 0 < x < 1:
        return a * x**2
    elif 1 <= x < 2:
        return a * (2 - x)**2
    else:
        return 0
#Định nghĩa hàm f(x, a):
#Hàm này mô tả hàm mật độ xác suất của biến ngẫu nhiên X, phụ thuộc vào tham số a.
#Hàm trả về giá trị mật độ xác suất tại điểm x.

# Tìm giá trị của a
def tim_a():
    tich_phan1 = tich_phan(lambda x: x**2, 0, 1)
    tich_phan2 = tich_phan(lambda x: (2 - x)**2, 1, 2)
    a = 1 / (tich_phan1 + tich_phan2)
    return a
# Định nghĩa hàm tim_a():
#Hàm này tìm giá trị của tham số a sao cho hàm mật độ xác suất được chuẩn hóa.
#Hàm tính toán tích phân của x^2 và (2 - x)^2 trên các khoảng tương ứng của hàm mật độ xác suất, 
#sau đó lấy nghịch đảo của tổng hai tích phân này để tìm a.

gia_tri_a = tim_a()
#Tìm giá trị của a:
#Gán giá trị của a được tìm bởi hàm tim_a() cho biến gia_tri_a.

# Giá trị kỳ vọng E[X]
def ky_vong(a):
    tich_phan1 = tich_phan(lambda x: x * a * x**2, 0, 1)
    tich_phan2 = tich_phan(lambda x: x * a * (2 - x)**2, 1, 2)
    return tich_phan1 + tich_phan2

E_X = ky_vong(gia_tri_a)
#Tính toán kỳ vọng E[X]:
#Định nghĩa hàm ky_vong(a) để tính toán kỳ vọng E[X] của biến ngẫu nhiên X.
#Hàm ky_vong(a) tính toán tích phân của x * f(x, a) trên các khoảng tương ứng của hàm mật độ xác suất và trả về giá trị của tích phân.
#Tính toán E_X bằng cách gọi hàm ky_vong(gia_tri_a) với gia_tri_a là giá trị đã tìm được trước đó.

# E[X^2]
def ky_vong_binh_phuong(a):
    tich_phan1 = tich_phan(lambda x: x**2 * a * x**2, 0, 1)
    tich_phan2 = tich_phan(lambda x: x**2 * a * (2 - x)**2, 1, 2)
    return tich_phan1 + tich_phan2

E_X2 = ky_vong_binh_phuong(gia_tri_a)
#Tính toán E[X^2]:
#Định nghĩa hàm ky_vong_binh_phuong(a) để tính toán kỳ vọng E[X^2] của biến ngẫu nhiên X.
#Hàm ky_vong_binh_phuong(a) tính toán tích phân của x^2 * f(x, a) trên các khoảng tương ứng của hàm mật độ xác suất và trả về giá trị của tích phân.
#Tính toán E_X2 bằng cách gọi hàm ky_vong_binh_phuong(gia_tri_a) với gia_tri_a là giá trị đã tìm được trước đó.

# Phương sai Var(X)
Phuong_sai_X = E_X2 - E_X**2
#Tính toán phương sai Var(X):
#Tính toán phương sai Var(X) bằng cách sử dụng công thức Var(X) = E[X^2] - E[X]^2.
#Gán giá trị của Phuong_sai_X cho biến Var(X).

# Độ lệch chuẩn
do_lech_chuan = Phuong_sai_X**0.5
#Tính toán độ lệch chuẩn:
#Tính toán độ lệch chuẩn bằng cách lấy căn bậc hai của phương sai.
#Gán giá trị của do_lech_chuan cho biến SD(X).

# Xác suất P(0.5 < X < 2)
def xac_suat(a):
    tich_phan1 = tich_phan(lambda x: a * x**2, 0.5, 1)
    tich_phan2 = tich_phan(lambda x: a * (2 - x)**2, 1, 2)
    return tich_phan1 + tich_phan2

P = xac_suat(gia_tri_a)
#Tính toán xác suất P(0.5 < X < 2):
#Định nghĩa hàm xac_suat(a) để tính toán xác suất P(0.5 < X < 2).
#Hàm xac_suat(a) tính toán tích phân của f(x, a) trên khoảng từ 0.5 đến 2 và trả về giá trị của tích phân.
#Tính toán P bằng cách gọi hàm xac_suat(gia_tri_a) với gia_tri_a là giá trị đã tìm được trước đó.

# In kết quả
print(f"Giá trị của a: {gia_tri_a}")
print(f"Kỳ vọng E[X]: {E_X}")
print(f"Phương sai Var(X): {Phuong_sai_X}")
print(f"Độ lệch chuẩn: {do_lech_chuan}")
print(f"P(0.5 < X < 2): {P}")
#In kết quả:
#In ra giá trị của a, E[X], Var(X), SD(X), và P(0.5 < X < 2).
