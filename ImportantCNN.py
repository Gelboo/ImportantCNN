## Data Augmentation ==> get better result because of generalization
# Rotation invariance translation invariance

# After importing the Data
from keras.preprocessing.image import ImageDataGenerator
# create and configure augmented image generator
datagen = ImageDataGenerator(
            width_shift_range=0.1,
            height_shift_range=0.1,
            horizontal_flip=True)
datagen.fit(x_train)
