import argparse

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers

from notebooks.dataset import get_class_names

def predict_singular(image_location, model_dir):
    def quality(_predicted_class, _predicted_confidence):
        predicted_type = 'Healthy' if 'Healthy' in _predicted_class else 'Rotten'
        if predicted_type == "Healthy":
            colour_score = min(100, int(75 + _predicted_confidence * 20))
            size_score = min(100, int(80 + _predicted_confidence * 15))
            ripeness_score = min(100, int(70 + _predicted_confidence * 20))
        else:
            colour_score = max(40, int(70 - _predicted_confidence * 20))
            size_score = max(40, int(75 - _predicted_confidence * 15))
            ripeness_score = max(40, int(65 - _predicted_confidence * 20))
        return {
            "colour_score": colour_score,
            "size_score": size_score,
            "ripeness_score": ripeness_score
        }

    def grading(colour_score, size_score, ripeness_score):
        if colour_score >= 75 and size_score >= 80 and ripeness_score >= 70:
            return "A"
        elif colour_score >= 65 and size_score >= 70 and ripeness_score >= 60:
            return "B"
        else:
            return "C"

    dataset_classes = get_class_names("dataset")
    loaded_model = tf.keras.models.load_model(model_dir)

    image = tf.io.read_file(image_location)
    image = tf.image.decode_image(image, channels=3, expand_animations=False)
    image_size = (244,244)
    image = tf.image.resize(image, image_size)
    image = tf.cast(image, tf.float32) / 255.0
    image_arr = tf.keras.utils.img_to_array(image)
    image_arr = np.expand_dims(image_arr, axis=0)

    prediction = loaded_model.predict(image_arr)
    prediction_index = np.argmax(prediction[0])
    predicted_class = dataset_classes[prediction_index]
    predicted_confidence = float(prediction[0][prediction_index])
    produce_type, freshness_label = predicted_class.split("__")
    quality_score = quality(predicted_class, predicted_confidence)
    grade = grading(quality_score["colour_score"], quality_score["size_score"], quality_score["ripeness_score"])
    return {
        "produce_type": produce_type,
        "freshness_label": freshness_label,
        "predicted_class": predicted_class,
        "confidence": round(predicted_confidence, 3),
        "colour_score": round(quality_score["colour_score"], 3),
        "size_score": round(quality_score["size_score"], 3),
        "ripeness_score": round(quality_score["ripeness_score"], 3),
        "grade": grade
    }


parser = argparse.ArgumentParser()
parser.add_argument('filename', nargs='+')
parser.add_argument('-m', '--model', type=str, required=True)
args = parser.parse_args()
image_path = args.filename[0]
print(predict_singular(image_path, args.model))

