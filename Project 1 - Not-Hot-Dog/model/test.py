import numpy as np
from tensorflow.keras.applications.vgg19 import preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

def get_prediction(path):
    image_width, image_height = 150, 150
    img = image.load_img(path, target_size=(image_width, image_height))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis = 0)
    img = preprocess_input(img)
    model = load_model('vgg_model.h5')
    prediction = model.predict_classes(img)
    return 'hotdog' if prediction[0][0] == 0 else 'not hotdog'


if __name__ == "__main__":
    print(get_prediction('new_test_images/1.png'))