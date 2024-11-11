from kalmanfilterByRuhail.core import KalmanFilter
import numpy as np

# Define system
F = np.array([[1]])
H = np.array([[1]])
Q = np.array([[0.1]])
R = np.array([[0.5]])
P = np.array([[1]])
x = np.array([[0]])

kf = KalmanFilter(F, H, Q, R, P, x)

# Simulated measurements
measurements = [1, 2, 3, 4, 5]
estimates = []

for z in measurements:
    kf.predict()
    kf.update(np.array([[z]]))
    estimates.append(kf.get_state()[0, 0])

print("Estimates:", estimates)
