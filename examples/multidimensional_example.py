from kalmanfilterByRuhail.core import KalmanFilter
import numpy as np

# Define multidimensional system parameters
F = np.array([[1, 1], [0, 1]])  # State transition matrix
H = np.array([[1, 0]])          # Measurement matrix
Q = np.array([[0.001, 0], [0, 0.001]])  # Process noise covariance
R = np.array([[1]])             # Measurement noise covariance
P = np.eye(2)                   # Initial estimate error covariance
x = np.array([[0], [1]])        # Initial state

kf = KalmanFilter(F, H, Q, R, P, x)

# Simulated measurements
measurements = [0.9, 2.1, 2.9, 4.1, 5.0]
estimates = []

for z in measurements:
    kf.predict()
    kf.update(np.array([[z]]))
    estimates.append(kf.get_state()[0, 0])

print("Estimates:", estimates)
