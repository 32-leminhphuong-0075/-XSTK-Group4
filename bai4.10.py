from collections import Counter

# Dữ liệu ban đầu
data_X = [4, 4, 4, 7, 7, 7, 7, 12, 12, 12, 17, 17]
data_Y = [90, 110, 130, 110, 130, 130, 150, 130, 150, 180, 90, 180]

# Tổng số điểm dữ liệu
total_data_points = len(data_X)

# Tính phân phối xác suất của X
count_X = Counter(data_X)
prob_X = {x: count / total_data_points for x, count in count_X.items()}
print("Phân phối xác suất của X:")
for x, prob in prob_X.items():
    print(f"P(X = {x}) = {prob:.3f}")

# Tính phân phối xác suất của Y
count_Y = Counter(data_Y)
prob_Y = {y: count / total_data_points for y, count in count_Y.items()}
print("\nPhân phối xác suất của Y:")
for y, prob in prob_Y.items():
    print(f"P(Y = {y}) = {prob:.3f}")

# Tính phân phối xác suất của X khi Y = 130
X_given_Y_130 = [data_X[i] for i in range(total_data_points) if data_Y[i] == 130]
count_X_given_Y_130 = Counter(X_given_Y_130)
total_Y_130 = len(X_given_Y_130)
prob_X_given_Y_130 = {x: count / total_Y_130 for x, count in count_X_given_Y_130.items()}
print("\nPhân phối xác suất của X đối với Y = 130:")
for x, prob in prob_X_given_Y_130.items():
    print(f"P(X = {x} | Y = 130) = {prob:.3f}")

# Tính phân phối xác suất của Y khi X = 12
Y_given_X_12 = [data_Y[i] for i in range(total_data_points) if data_X[i] == 12]
count_Y_given_X_12 = Counter(Y_given_X_12)
total_X_12 = len(Y_given_X_12)
prob_Y_given_X_12 = {y: count / total_X_12 for y, count in count_Y_given_X_12.items()}
print("\nPhân phối xác suất của Y đối với X = 12:")
for y, prob in prob_Y_given_X_12.items():
    print(f"P(Y = {y} | X = 12) = {prob:.3f}")

# Kiểm tra tính độc lập của X và Y
joint_prob = Counter(zip(data_X, data_Y))
independent = True
for (x, y), joint_count in joint_prob.items():
    joint_p = joint_count / total_data_points
    if not (joint_p == prob_X[x] * prob_Y[y]):
        independent = False
        break

print("\nX và Y có độc lập không?")
print("Có" if independent else "Không")
#In kết quả kiểm tra tính độc lập:*
#In kết quả cuối cùng về tính độc lập của \(X\) và \(Y\).

