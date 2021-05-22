from keras.datasets import fashion_mnist
import matplotlib.pyplot as plt
import tensorflow as tf
from keras import datasets, layers, models, losses

fashion_mnist = fashion_mnist

(train_images, train_labels), (test_imanges, test_labels) = fashion_mnist.load_data()

# Print a few samples from these four arrays, for example, the training labels as follows:
print(train_labels)

# The label arrays do not include class names. Hence, we define them as follows and will
# use them for plotting later on:
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt',
               'Sneaker', 'Bag', 'Ankle boot']

# Take a look at the format of the image
print(train_images.shape)

# Similarly for the 10000 testing samples, we check the format as follows:
print(test_imanges.shape)

# Let's now inspect a random training sample
plt.figure()
plt.imshow(train_images[42])
plt.colorbar()
plt.grid(False)
plt.title(class_names[train_labels[42]])

plt.savefig('Fashion_MNIST.jpg')

plt.show()

# In the ankle boot sample, the pixel values are in the range of 0 to 255.
# Hence, we need to rescale the data to a range of 0 to 1 before feeding it to the neural network.
train_images = train_images / 255.0
test_images = test_imanges / 255.0

# Now we display the first 16  training samples after the pre-processing
for i in range(16):
    plt.subplot(4, 4, i + 1) # Do not mistake subplot as subplots [1]
    plt.subplots_adjust(hspace=.3)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)

    plt.imshow(train_images[i], cmap=plt.cm.binary)

    plt.title(class_names[train_labels[i]])


plt.savefig('Fashion_MINIST_.jpg')
plt.show()

# As the convolutional layer in Keras only takes in individual samples in three dimensions,
# we need to first reshape the data into four dimensions:
X_train = train_images.reshape((train_images.shape[0], 28, 28, 1))

X_test = test_images.reshape((test_imanges.shape[0], 28, 28, 1))

print(X_train.shape)

# Before we develop the CNN model, let's specify the random speed in TensorFlow for reproducibility
tf.random.set_seed(42)

model = models.Sequential()

# For the convolutional extractor, we are going to use three convolutional layers.

## We start with the first convolutional layer with 32 small-sized 3 * 3 filters.
model.add(layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))

## The first convolutional layer is followed by a max-pooling layer with a 2 * 2 filter
model.add(layers.MaxPooling2D(pool_size=(2, 2)))

## The second convolutional layer with 64 3 * 3 filters.
model.add(layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))

## The max-pooling layer paired with the second convolutional layer.
model.add(layers.MaxPooling2D(pool_size=(2, 2)))

## The third convolutional layer with 128 3 * 3 filters.
model.add(layers.Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))



# References:
# 1. https://stackoverflow.com/q/57383760/14900011