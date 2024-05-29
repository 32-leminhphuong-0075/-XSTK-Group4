def calculate_c():
    return 2 / 3

def F(x, y, z):
    c = calculate_c()
    return c * (x**2 * y * z / 3 + y**2 * x * z / 3 + z**2 * x * y / 3)

# Test các giá trị
x, y, z = 1, 1, 1
print("c:", calculate_c())
print("F(x, y, z):", F(x, y, z))