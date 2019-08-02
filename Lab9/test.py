from __future__ import absolute_import, division, print_function

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from PIL import Image
from PIL import ImageOps

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  
  plt.imshow(img, cmap=plt.cm.binary)
  
  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'
  
  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array[i], true_label[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)
  
  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

# Test tensorflow install
# print(tf.__version__)
# plt.plot((-2,4),(-6,6))
# plt.show()

# downloads the dataset
fashion_mnist = keras.datasets.fashion_mnist

# (train set), (test_set)
# the images are 28x28 NumPy arrays, with pixel values of 0 through 9, representing class_names
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# map each array index to its type
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# the number of images, and the size of the arrays
train_images.shape

# labels in the traning set
len(train_labels)

# labels on the data
train_labels

# the shape of test labels
test_images.shape

# the number of images
len(test_labels)

# An example of how a single image has a value from [0, 255] per pixel
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

# nice pythonic syntax to scale values into the [0-1] range
train_images = train_images / 255.0

test_images = test_images / 255.0

# display the first 25 images
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()

# setup layers
# the .Flatten layer transfroms the 2D array of images to a 1D array, unrolling the matrix.
# the network uses 2 .Dense layers to score the images into certain classes.
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

# compile the model by picking the optimizer, the loss function, and the metrics used to track training.
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#
#
#
# This actually trains the model. In the tutorial, the model should be about 88% accurate.
# This uses 5 epochs to train. 
model.fit(train_images, train_labels, epochs=5)
#
#
#
#

# print out the performance of the model
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)

# Now, predict the classes of the test dataset using the trained model.
predictions = model.predict(test_images)

# Look at the first prediction.
predictions[0]

# And get the highest confidence value
np.argmax(predictions[0])

# And the class it falls into:
test_labels[0]

# look at the 0th image, and the prediction array for that image.
i = 0
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions, test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions,  test_labels)
plt.show()

# and the same for the 12th
i = 12
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions, test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions,  test_labels)
plt.show()

# Plot the first X test images, their predicted label, and the true label
# Color correct predictions in blue, incorrect predictions in red
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(9000, 9015):
  plt.subplot(num_rows, 2*num_cols, 2*(i - 9000)+1)
  plot_image(i, predictions, test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*(i - 9000)+2)
  plot_value_array(i, predictions, test_labels)
plt.show()

# Grab an image from the test dataset
img = test_images[0]

print(img.shape)

# Add the image to a batch where it's the only member.
img = (np.expand_dims(img,0))

print(img.shape)

# Run prediction on that single image
predictions_single = model.predict(img)

print(predictions_single)

# Plot the numpy array that is generated. This shows its confidence in each category
#  for the test input.
plot_value_array(0, predictions_single, test_labels)
plt.xticks(range(10), class_names, rotation=45)
plt.show()

# The prediction result is the highest confidence value in the matrix.
prediction_result = np.argmax(predictions_single[0])
print(prediction_result)