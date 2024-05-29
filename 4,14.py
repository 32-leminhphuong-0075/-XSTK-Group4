import numpy as np
# Đầu tiên, chúng ta import thư viện NumPy để sử dụng các tính năng tính toán số học

#Tiếp theo, chúng ta khai báo ma trận `joint_probabilities`, chứa xác suất đồng thời của các cặp (X, Y)
joint_probabilities = np.array([[0.415, 0.015, 0.115],
                                [0.115, 0.215, 0.020],
                                [0.115, 0.200, 0.015]])
# Sau đó, chúng ta tính các phân phối xác suất biên của X và Y bằng cách tính tổng các xác suất theo các cột và hàng tương ứng của ma trận `joint_probabilities`

marginal_prob_X = np.sum(joint_probabilities, axis=0)
marginal_prob_Y = np.sum(joint_probabilities, axis=1)

# Tiếp theo, chúng ta tính kỳ vọng của X và Y bằng cách nhân mỗi giá trị X hoặc Y với phân phối xác suất biên tương ứng và sau đó tính tổng
expected_X = np.sum([-1, 0, 1] * marginal_prob_X)
expected_Y = np.sum([-1, 0, 1] * marginal_prob_Y)

# Tính kỳ vọng của X*Y
# Chúng ta tính kỳ vọng của X*Y bằng cách nhân mỗi cặp giá trị X và Y với xác suất tương ứng từ ma trận xác suất đồng thời và sau đó tính tổng

expected_XY = np.sum(np.outer([-1, 0, 1], [-1, 0, 1]) * joint_probabilities)

# Tính Cov(X, Y)
# Tiếp theo, chúng ta tính hiệp phương sai (covariance) của X và Y bằng cách trừ kỳ vọng của X*Y với tích của kỳ vọng của X và Y
cov_XY = expected_XY - expected_X * expected_Y
# Tính phương sai của X và Y
expected_X2 = np.sum([(-1)**2, 0**2, 1**2] * marginal_prob_X)
expected_Y2 = np.sum([(-1)**2, 0**2, 1**2] * marginal_prob_Y)

var_X = expected_X2 - expected_X**2
var_Y = expected_Y2 - expected_Y**2
# Chúng ta tính phương sai của X và Y bằng cách tính kỳ vọng của \(X^2\) và \(Y^2\) sau đó trừ đi bình phương của kỳ vọng của X và Y

# Tính hệ số tương quan
corr_coefficient = cov_XY / (np.sqrt(var_X) * np.sqrt(var_Y))
# Cuối cùng, chúng ta tính hệ số tương quan (correlation coefficient) giữa X và Y bằng cách chia hiệp phương sai của X và Y cho tích của độ lệch chuẩn của X và Y

print("1) Phân phối xác suất biên của X:", marginal_prob_X)
print("   Phân phối xác suất biên của Y:", marginal_prob_Y)
print("2) Kỳ vọng của X:", expected_X)
print("   Kỳ vọng của Y:", expected_Y)
print("   Kỳ vọng của X*Y:", expected_XY)
print("   Cov(X, Y):", cov_XY)
print("3) Hệ số tương quan (correlation coefficient) giữa X và Y:", corr_coefficient)