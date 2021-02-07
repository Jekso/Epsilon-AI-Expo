from flask import Flask, jsonify, request
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg19 import preprocess_input
import base64
from PIL import Image
from io import BytesIO

# __name__ is equal to app.py
app = Flask(__name__)

model = load_model('vgg_model.h5')


def get_prediction(path):
    image_width, image_height = 150, 150
    img = image.load_img(path, target_size=(image_width, image_height))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis = 0)
    img = preprocess_input(img)
    prediction = model.predict_classes(img)
    return 'hotdog' if prediction[0][0] == 0 else 'not hotdog'


@app.route("/predict", methods=["POST"])
def predict():
	base64_img = request.json['image']
	im = Image.open(BytesIO(base64.b64decode(base64_img)))
	im.save('test.png', 'PNG')
	prediction = get_prediction('test.png')
	return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')