from kalmanfilterByRuhail.extended import ExtendedKalmanFilter
import numpy as np

# Define nonlinear system
def f(x):
    return np.array([[x[0, 0] + x[1, 0] * np.cos(x[0, 0])], [x[1, 0]]])

def h(x):
    return np.array([[x[0, 0]**2]])

def F_jacobian(x):
    return np.array([[1, -np.sin(x[0, 0])], [0, 1]])

def H_jacobian(x):
    return np.array([[2 * x[0, 0], 0]])

F = np.eye(2)
H = np.array([[1, 0]])
Q = np.eye(2) * 0.01
R = np.array([[1]])
P = np.eye(2)
x = np.array([[0.5], [1]])

ekf = ExtendedKalmanFilter(F, H, Q, R, P, x, f, h, F_jacobian, H_jacobian)

# Simulated measurements
measurements = [0.25, 0.8, 2.1, 3.2, 4.9]
estimates = []

for z in measurements:
    ekf.predict()
    ekf.update(np.array([[z]]))
    estimates.append(ekf.get_state()[0, 0])

print("EKF Estimates:", estimates)
