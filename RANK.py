# Importing the necessary libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense

def get_output():
    # Defining the data
    data = pd.read_csv("S1234.csv")

    # Reshaping the data
    values = data['RANK'][1:50].values.reshape(-1, 1)

    # Normalizing the data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(values)
    scaled_data = scaled_data.reshape(scaled_data.shape[0], 1, scaled_data.shape[1])

    # Building the LSTM model
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(1, 1)))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')

    # Fitting the model
    model.fit(scaled_data, scaled_data, batch_size=1, epochs=5)

    # Getting the predictions for all values and the next value
    scaled_predictions = model.predict(scaled_data)
    scaled_next_prediction = model.predict(np.array([[scaled_predictions[-1]]]))

    # Reshape the predictions back to 2D
    scaled_predictions = scaled_predictions.reshape(scaled_predictions.shape[0],)
    unscaled_predictions = scaler.inverse_transform(scaled_predictions.reshape(-1, 1))
    # Inverse scaling to get the predictions in the original scale
    predictions = scaler.inverse_transform(scaled_predictions.reshape(-1, 1))
    next_prediction = scaler.inverse_transform(scaled_next_prediction)

    # Print all the predicted values and the next value
    #print("All predicted values: {}".format(predictions.ravel()))
    print("Next predicted value: {}".format(next_prediction[0][0]))

    #Calculate mean squared error and standard deviation
    mse = np.mean((scaled_predictions - scaled_data)**2)
    mse_rounded = round(mse, 4)
    std_dev = np.sqrt(mse)
    std_dev_rounded = round(std_dev, 4)
    print("Mean squared error: {}".format(mse_rounded))
    print("Standard deviation: {}".format(std_dev_rounded))

    # To display in GUI
    Ypred = round(next_prediction[0][0] / 2097.45, 4)
    print(Ypred)

    min_range = round((next_prediction[0][0] - std_dev) / 2097.45 , 4)
    print(min_range)

    max_range = round((next_prediction[0][0] + std_dev) / 2097.45 , 4)
    print(max_range)

    return Ypred, mse_rounded, std_dev_rounded, min_range, max_range
