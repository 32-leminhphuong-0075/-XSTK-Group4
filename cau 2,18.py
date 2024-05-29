
# Hàm tính tích phân của x * f(x) trên đoạn [1, 4]
def integral_x_fx():
    def f(x):
        return 3 * (1 - x / 4)
    
    # Tích phân của x * f(x)
    def integrand(x):
        return x * f(x)
    
    # Chia đoạn [1, 4] thành n phần nhỏ để tính tích phân
    n = 1000000
    a = 1
    b = 4
    dx = (b - a) / n
    integral = 0
    
    for i in range(n):
        x = a + i * dx
        integral += integrand(x) * dx
    
    return integral

# Hàm tính tích phân của x^2 * f(x) trên đoạn [1, 4]
def integral_x2_fx():
    def f(x):
        return 3 * (1 - x / 4)
    
    # Tích phân của x^2 * f(x)
    def integrand(x):
        return x * x * f(x)
    
    # Chia đoạn [1, 4] thành n phần nhỏ để tính tích phân
    n = 1000000
    a = 1
    b = 4
    dx = (b - a) / n
    integral = 0
    
    for i in range(n):
        x = a + i * dx
        integral += integrand(x) * dx
    
    return integral

# Tính kỳ vọng E[X]
E_X = integral_x_fx()
print(f'Kỳ vọng E[X]: {E_X}')

# Tính E[X^2]
E_X2 = integral_x2_fx()
print(f'E[X^2]: {E_X2}')

# Tính phương sai Var(X)
Var_X = E_X2 - E_X**2
print(f'Phương sai Var(X): {Var_X}')

# Tìm mốt của X
# Vì f(x) = 3(1 - x/4) là hàm bậc nhất giảm dần, mốt sẽ nằm ở giá trị nhỏ nhất của x trong đoạn [1, 4]
mode = 1
print(f'Mốt của X: {mode}')