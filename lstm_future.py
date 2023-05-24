# Import necessary libraries
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

# Load and prepare the dataset
data = pd.read_csv('SEQ_567_Predictions.csv')
data = data['S5'][1000:3000].values.reshape(-1, 1)
data = data.astype('float32')

# Normalize the data
scaler = MinMaxScaler(feature_range=(0, 1000))  # change the feature range to (0, 1000)
data = scaler.fit_transform(data)

# Split the data into train and test sets
train_size = int(len(data) * 0.8)
test_size = len(data) - train_size
train, test = data[0:train_size,:], data[train_size:len(data),:]

# Create sequences of input/output pairs
def create_dataset(dataset, look_back=1):
    X, Y = [], []
    for i in range(len(dataset)-look_back-1):
        X.append(dataset[i:(i+look_back), 0])
        Y.append(dataset[i+look_back, 0])
    return np.array(X), np.array(Y)

look_back = 5
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)
trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))

# Define and train the LSTM model
model = Sequential()
model.add(LSTM(128, return_sequences=True, input_shape=(1, look_back)))
model.add(LSTM(128, return_sequences=False))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, epochs=500, batch_size=8, verbose=2)

# Use the LSTM model to predict the next 10 values
last_sequence = data[-look_back:]
next_10_predictions = []
for i in range(10):
    next_prediction = model.predict(last_sequence.reshape(1, 1, look_back))
    next_10_predictions.append(scaler.inverse_transform(next_prediction)[0, 0])
    last_sequence = np.append(last_sequence[1:], next_prediction)


def get_predictions():
    # Use the LSTM model to predict the next 10 values
    last_sequence = data[-look_back:]
    next_10_predictions = []
    for i in range(10):
        next_prediction = model.predict(last_sequence.reshape(1, 1, look_back))
        next_10_predictions.append(scaler.inverse_transform(next_prediction)[0, 0])
        last_sequence = np.append(last_sequence[1:], next_prediction)

    return next_10_predictions


print("Predicted values for the next 10 time steps:")
print(next_10_predictions)
