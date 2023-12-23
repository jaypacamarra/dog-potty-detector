# Detect dog, poop, stance

import cv2
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions

# Load the pre-trained MobileNetV2 model
model = MobileNetV2(weights='imagenet')

# Function to classify the image using the MobileNetV2 model
def classify_image(img):
    # Resize the image to the required input size for MobileNetV2 (224x224)
    img = cv2.resize(img, (224, 224))
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)

    # Make predictions
    predictions = model.predict(img)
    decoded_predictions = decode_predictions(predictions)

    classid = np.argmax(predictions)
    return classid

dog_id_list = {
    151,
    153,
    229,
    268,
    281,
    296,
    302,
    303,
    304,
    305,
    306,
    307,
    308,
    309,
    310
}

def is_dog(classid):
    is_dog = classid in dog_id_list
    return is_dog
