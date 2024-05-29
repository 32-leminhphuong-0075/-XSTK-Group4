def p_x(x, c):
    return c * (1/3)**x

def expected_value(c):
    expectation = 0
    x = 0
    while True:
        term = x * p_x(x, c)
        if term < 1e-10:  # Dừng khi giá trị của term rất nhỏ, gần bằng 0
            break
        expectation += term
        x += 1
    return expectation

def p_x_geq_3(c):
    probability = 0
    x = 3
    while True:
        term = p_x(x, c)
        if term < 1e-10:  # Dừng khi giá trị của term rất nhỏ, gần bằng 0
            break
        probability += term
        x += 1
    return probability

def p_x_eq_2k_1(k, c):
    x = 2 * k + 1
    return p_x(x, c)

# Giá trị c
c = 2 / 3
print("c:",c)

# Tính giá trị E(X)
E_X = expected_value(c)
print("E(X):", E_X)

# Tính P(X >= 3)
P_X_geq_3 = p_x_geq_3(c)
print("P(X >= 3):", P_X_geq_3)

# Tính P(X = 2k + 1) với k = 1
k = 1
P_X_eq_2k_1 = p_x_eq_2k_1(k, c)
print("P(X = 2k + 1) với k =", k, ":", P_X_eq_2k_1)