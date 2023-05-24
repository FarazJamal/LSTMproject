# Importing the necessary libraries
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, Dense

# Defining the data
#data = np.array([7.661, 7.161, 8.102, 7.549, 7.408, 7.289, 7.269, 5.755, 7.896, 7.363, 7.258, 6.112, 6.753, 7.269,7.584,8.254,6.826,7.573,6.232,8.123,7.176, 8.034,7.199,8.372,7.056,7.818,7.382,6.759,7.872,7.356, 7.889,7.952,8.064, 8.573, 7.384, 8.016, 8.345, 8.345, 6.791, 8.428])
data = pd.read_csv("Sequences_.csv")
# Reshaping the data
values = data['S1'][:180].values
data = values.reshape(-1, 1)

# Building the LSTM model
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(1, 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')

# Fitting the model
model.fit(data, data, batch_size=1, epochs=100)

# Getting the predictions
predictions = model.predict(data)


mse = np.mean((predictions - data)**2)
std = np.std(predictions - data)

print("Mean Square Error (MSE): {:.4f}".format(mse))
print("Standard Deviation (STD): {:.4f}".format(std))

# Plotting the real and predicted values
plt.plot(data, label='Real Values')
plt.plot(predictions, label='Predicted Values')
plt.legend()
plt.show()
