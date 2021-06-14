from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN
import Time_Series_Generator as time

number_of_steps = 50
series = time.generate_time_series(batch_size=10000, number_of_steps=number_of_steps + 1)

X_train, y_train = series[:7000, :number_of_steps], series[:7000, -1]
X_valid, y_valid = series[7000:9000, :number_of_steps], series[7000:9000, -1]
X_test, y_test = series[9000:, :number_of_steps], series[9000:, -1]

model = Sequential([SimpleRNN(units=20, return_sequences=True, input_shape=[None, 1]),
                    SimpleRNN(units=20, return_sequences=True),
                    SimpleRNN(units=1)])




