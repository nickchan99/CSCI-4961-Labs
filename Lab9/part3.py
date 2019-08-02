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

# map each array index to its type
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

my_labels = []
my_images = []

sleeveless = Image.open("sleeveless.png")
sleeveless_grey = ImageOps.invert( ImageOps.grayscale(sleeveless) )
sleeveless_grey = sleeveless_grey.resize( (28,28) ) 
arr = np.asarray( sleeveless_grey ) / 255.0 
sleeveless_grey = ImageOps.invert(sleeveless_grey)
sleeveless_grey.save("sleeveless_grey.png", "PNG")
my_images.append(arr)
# The top is technically a top, but I expect it to be mapped to a dress.
my_labels.append(0)
sleeveless.close()

yeezy = Image.open("yeezy.png")
yeezy_grey = ImageOps.invert( ImageOps.grayscale(yeezy) )
yeezy_grey = yeezy_grey.resize( (28,28) ) 
arr = np.asarray( yeezy_grey ) / 255.0 
yeezy_grey = ImageOps.invert(yeezy_grey)
yeezy_grey.save("yeezy_grey.png", "PNG")
my_images.append(arr)
# Yeezy is a sneaker
my_labels.append(7)
yeezy.close()

jersey = Image.open("jersey.png")
jersey_grey = ImageOps.invert( ImageOps.grayscale(jersey) )
jersey_grey = jersey_grey.resize( (28,28) )
arr = np.asarray( jersey_grey ) / 255.0 
jersey_grey = ImageOps.invert(jersey_grey)
jersey_grey.save("jersey_grey.png", "PNG")
my_images.append(arr)
# The jersey is a top
my_labels.append(0)
jersey.close()

my_images = np.array(my_images)
my_labels = np.array(my_labels)

# display the images

plt.figure(figsize=(10,10))
for i in range(3):
    plt.subplot(1,3,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(my_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[my_labels[i]])
plt.show()

# downloads the dataset
fashion_mnist = keras.datasets.fashion_mnist

# (train set), (test_set)
# the images are 28x28 NumPy arrays, with pixel values of 0 through 9, representing class_names
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

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

predictions = model.predict(my_images)

# Plot the first X test images, their predicted label, and the true label
# Color correct predictions in blue, incorrect predictions in red
num_rows = 1
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions, my_labels, my_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions, my_labels)
plt.show()