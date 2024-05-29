# Bước 1: Tìm hệ số A
A = 0
for x in range(1, 11):
    for y in range(1, 11):
        A += x * y
A *= 0.01  # Vì x và y đều trong khoảng từ 1 đến 10, tổng có 100 phần tử

print("Hệ số A:", A)

# Bước 2: Tìm f_X(x) và f_Y(y)
f_X = 0
for y in range(1, 11):
    f_X += y
f_X *= 0.01  # Tổng của y từ 1 đến 10 có 10 phần tử

f_Y = 0
for x in range(1, 11):
    f_Y += x
f_Y *= 0.01  # Tổng của x từ 1 đến 10 có 10 phần tử

print("f_X(x):", f_X)
print("f_Y(y):", f_Y)

# Bước 3: Kiểm tra tính độc lập của X và Y
f = lambda x, y: x * y
independence_check = 0
for x in range(1, 11):
    for y in range(1, 11):
        independence_check += f(x, y) - f_X * f_Y

if independence_check == 0:
    print("X và Y là độc lập.")
else:
    print("X và Y không độc lập.")
