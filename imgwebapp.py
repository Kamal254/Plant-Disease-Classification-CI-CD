# import warnings
# warnings.simplefilter(action='ignore', category=FutureWarning)

# import tensorflow as tf
# import numpy as np
# import streamlit as st
# from PIL import Image
# import requests
# from io import BytesIO

# st.set_option('deprecation.showfileUploaderEncoding', False)
# st.title("Plant Disease Image Classifier")
# st.text("Provide URL of plant image for classification")

# @st.cache(allow_output_mutation=True)
# def load_model():
#   model = tf.keras.models.load_model('/app/models/')
#   return model

# with st.spinner('Loading Model Into Memory....'):
#   model = load_model()

# classes=['Tomato___Late_blight', 'Tomato___healthy', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Potato___healthy', 'Corn_(maize)___Northern_Leaf_Blight', 'Tomato___Early_blight', 'Tomato___Septoria_leaf_spot', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Strawberry___Leaf_scorch', 'Peach___healthy', 'Apple___Apple_scab', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Bacterial_spot', 'Apple___Black_rot', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Peach___Bacterial_spot', 'Apple___Cedar_apple_rust', 'Tomato___Target_Spot', 'Pepper,_bell___healthy', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Potato___Late_blight', 'Tomato___Tomato_mosaic_virus', 'Strawberry___healthy', 'Apple___healthy', 'Grape___Black_rot', 'Potato___Early_blight', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Common_rust_', 'Grape___Esca_(Black_Measles)', 'Raspberry___healthy', 'Tomato___Leaf_Mold', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Pepper,_bell___Bacterial_spot', 'Corn_(maize)___healthy']

# def decode_img(image):
#   img = tf.image.decode_jpeg(image, channels=3)  
#   img = tf.image.resize(img,[256,256])
#   return np.expand_dims(img, axis=0)

# path = st.text_input('Enter Image URL to Classify.. ','https://beanipm.pbgworks.org/sites/pbg-beanipm7/files/styles/picture_custom_user_wide_1x/public/AngularLeafSpotFig1a.jpg')
# if path is not None:
#     content = requests.get(path).content

#     st.write("Predicted Class :")
#     with st.spinner('classifying.....'):
#       label =np.argmax(model.predict(decode_img(content)),axis=1)
#       st.write(classes[label[0]])    
#     st.write("")
#     image = Image.open(BytesIO(content))
#     st.image(image, caption='Classifying Plant Disease', use_column_width=True)



import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import tensorflow as tf
import numpy as np
import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.title("Plant Disease Image Classifier")
st.text("Provide URL of plant image for classification")

@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('/app/models/')  # Update the path to your model
    return model

with st.spinner('Loading Model Into Memory....'):
    model = load_model()

classes = [
    'Tomato___Late_blight', 'Tomato___healthy', 'Grape___healthy', 
    'Orange___Haunglongbing_(Citrus_greening)', 'Soybean___healthy', 
    'Squash___Powdery_mildew', 'Potato___healthy', 
    'Corn_(maize)___Northern_Leaf_Blight', 'Tomato___Early_blight', 
    'Tomato___Septoria_leaf_spot', 
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
    'Strawberry___Leaf_scorch', 'Peach___healthy', 'Apple___Apple_scab', 
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Bacterial_spot', 
    'Apple___Black_rot', 'Blueberry___healthy', 
    'Cherry_(including_sour)___Powdery_mildew', 'Peach___Bacterial_spot', 
    'Apple___Cedar_apple_rust', 'Tomato___Target_Spot', 
    'Pepper,_bell___healthy', 
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Potato___Late_blight', 
    'Tomato___Tomato_mosaic_virus', 'Strawberry___healthy', 
    'Apple___healthy', 'Grape___Black_rot', 'Potato___Early_blight', 
    'Cherry_(including_sour)___healthy', 'Corn_(maize)___Common_rust_', 
    'Grape___Esca_(Black_Measles)', 'Raspberry___healthy', 
    'Tomato___Leaf_Mold', 
    'Tomato___Spider_mites Two-spotted_spider_mite', 
    'Pepper,_bell___Bacterial_spot', 'Corn_(maize)___healthy'
]

def decode_img(image):
    img = tf.image.decode_jpeg(image, channels=3)
    img = tf.image.resize(img, [256, 256])
    return np.expand_dims(img, axis=0)

path = st.text_input('Enter Image URL to Classify..', 'https://beanipm.pbgworks.org/sites/pbg-beanipm7/files/styles/picture_custom_user_wide_1x/public/AngularLeafSpotFig1a.jpg')
if path:
    content = requests.get(path).content

    st.write("Predicted Class:")
    with st.spinner('classifying.....'):
        label = np.argmax(model.predict(decode_img(content)), axis=1)
        st.write(classes[label[0]])
    st.write("")
    image = Image.open(BytesIO(content))
    st.image(image, caption='Classifying Plant Disease', use_column_width=True)
