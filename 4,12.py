import numpy as np
from scipy.integrate import quad
  # - `numpy` để thực hiện các phép toán số học và tích integration.
  #- `scipy.integrate.quad` để tính toán tích phân số.

# Định nghĩa hàm mật độ xác suất f(x, y)
def f(x, y):
    if 0 <= x <= 1 and 0 <= y <= 1:
        return (2/5) * (x + y)
    else:
        return 0
# Dịnh nghĩa hàm mật độ xác suất \( f(x, y) \)
# Hàm này nhận vào hai giá trị x và y, và trả về giá trị của hàm mật độ xác suất tại điểm đó

# Hàm mật độ xác suất biên của X
def f_X(x):
    return (2/5) * (x + 0.5)

# Hàm mật độ xác suất biên của Y
def f_Y(y):
    return (2/5) * (0.5 + y)

# Định nghĩa hàm mật độ xác suất biên của X và Y.
#  Đối với X, chúng ta tính tổng các giá trị của hàm mật độ xác suất theo y từ 0 đến 1.
#  Đối với Y, chúng ta tính tổng các giá trị của hàm mật độ xác suất theo x từ 0 đến 1.

# Hàm mật độ xác suất có điều kiện của X khi đã biết Y
def f_X_given_Y(x, y):
    return (x + y) / (0.5 + y)

# Hàm mật độ xác suất có điều kiện của Y khi đã biết X
def f_Y_given_X(y, x):
    return (x + y) / (x + 0.5)
# Định nghĩa hàm mật độ xác suất có điều kiện của X khi đã biết Y và của Y khi đã biết X.
# Cả hai hàm này đều được tính bằng cách chia hàm mật độ xác suất đồng thời \( f(x, y) \) cho hàm mật độ xác suất biên tương ứng.

# Tính kỳ vọng của X
E_X, _ = quad(lambda x: x * f_X(x), 0, 1)

# Tính kỳ vọng của Y
E_Y, _ = quad(lambda y: y * f_Y(y), 0, 1)

# Tính phương sai của X
E_X2, _ = quad(lambda x: x**2 * f_X(x), 0, 1)
V_X = E_X2 - E_X**2

# Tính phương sai của Y
E_Y2, _ = quad(lambda y: y**2 * f_Y(y), 0, 1)
V_Y = E_Y2 - E_Y**2

# Tính kỳ vọng có điều kiện của X khi đã biết Y
def E_X_given_Y(y):
    return quad(lambda x: x * f_X_given_Y(x, y), 0, 1)[0]

# Tính kỳ vọng có điều kiện của Y khi đã biết X
def E_Y_given_X(x):
    return quad(lambda y: y * f_Y_given_X(y, x), 0, 1)[0]

print("1) Hàm mật độ xác suất biên của X:")
print("   f_X(x) =", f_X(0.5)) # Ví dụ tính tại x = 0.5
print("2) Hàm mật độ xác suất biên của Y:")
print("   f_Y(y) =", f_Y(0.5)) # Ví dụ tính tại y = 0.5
print("3) Kỳ vọng của X:", E_X)
print("   Kỳ vọng của Y:", E_Y)
print("   Phương sai của X:", V_X)
print("   Phương sai của Y:", V_Y)
print("4) Kỳ vọng có điều kiện của X khi đã biết Y:")
print("   E(X|y=0.5) =", E_X_given_Y(0.5)) # Ví dụ tính tại y = 0.5
print("5) Kỳ vọng có điều kiện của Y khi đã biết X:")
print("   E(Y|x=0.5) =", E_Y_given_X(0.5)) # Ví dụ tính tại x = 0.5