# import need libraries 
import numpy as np
import matplotlib.pyplot as plt

# Initialize the data samples 

x_data = np.array([35., 38., 31., 20., 22., 25., 17., 60., 8., 60.])
Y_data= np.array([129.54611622, 135.54611622, 121.54611622, 99.54611622,
103.54611622, 109.54611622, 93.54611622, 179.54611622, 75.54611622, 179.54611622])

print(x_data)




def gradient_descent(x_data, Y_data, b:float, iterations: int, leazrn_rate: float, b_history: list, w_history: list):
    for i in range(iterations):
        y_pred = w * x_data + b

        grad_w = (2/len(x_data) * np.dot(x_data, y_pred - Y_data))
        grad_y = (2/len(x_data) * np.sum(y_pred - Y_data))

        w = w - learning_rate * grad_w
        b = b - learning_rate * grad_b

        b_history.append(b)
        w_history.append(w)