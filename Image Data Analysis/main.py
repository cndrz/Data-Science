import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Reshape
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Load MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Display dataset shapes
print(f"Training Data Shape: {x_train.shape}")
print(f"Training Labels Shape: {y_train.shape}")
print(f"Test Data Shape: {x_test.shape}")
print(f"Test Labels Shape: {y_test.shape}")

# Display a few images and their labels
plt.figure(figsize = (10, 10))
for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_train[i], cmap = cm.binary)
    plt.xlabel(y_train[i])
plt.show()

model = Sequential([
    Reshape((28, 28, 1), input_shape = (28, 28)),
    Conv2D(32, (3, 3), activation = "relu"),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation = "relu"),
    MaxPooling2D((2, 2)),
    Dense(64, activation = "relu"),
    Dense(10, activation = "softmax")
])

model.compile(optimizer = "adam", loss = "sparse_categorical_crossentropy", metrics = ["accuracy"])

# Train the model
history = model.fit(x_train, y_train, epochs = 10, validation_data = (x_test, y_test))

test_loss, test_acc = model.evaluate(x_test, y_test, verbose = 2)
print(f"Test Accuracy: {test_acc}")
