import streamlit as st
import cv2
import av
import pandas as pd
import numpy as np
import tensorflow as tf
from abc import ABC
from PIL import Image
from object_detection.utils import label_map_util
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer
from util import info, notify


CLASS_NAMES = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

PATH_TO_LABELS = 'label_map.pbtxt'
category_index = label_map_util.create_categories_from_labelmap(PATH_TO_LABELS, use_display_name=True)
CLASSES = []
for item in category_index:
    CLASSES.append(item['name'])


class VideoTransformer(VideoTransformerBase, ABC):
    # @st.cache(allow_output_mutation=True)
    def recv(self, frame):
        img = frame.to_ndarray(format='bgr24')
        config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
        weights_path = 'frozen_inference_graph.pb'
        net = cv2.dnn_DetectionModel(weights_path, config_file)
        net.setInputSize(320, 320)
        net.setInputScale(1.0 / 127.5)
        net.setInputMean((127.5, 127.5, 127.5))
        net.setInputSwapRB(True)
        font_scale = 1
        font = cv2.FONT_HERSHEY_COMPLEX

        class_index, confidence, bbox = net.detect(img, confThreshold=0.5)
        print(class_index, confidence, bbox)
        # dataframe('hello')
        for ClassInd, conf, boxes in zip(class_index.flatten(), confidence.flatten(), bbox):
            cv2.rectangle(img, boxes, (0, 255, 0), thickness=2)
            cv2.putText(img, CLASSES[ClassInd - 1], (boxes[0] + 10, boxes[1]), font, fontScale=font_scale,
                        color=(0, 0, 255), thickness=1)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return av.video.VideoFrame.from_ndarray(img, format='rgb24')


def image_ob():
    img = st.file_uploader("upload a file")
    if img is not None:
        img = cv2.imdecode(np.frombuffer(img.read(), np.uint8), -1)

        config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
        weights_path = 'frozen_inference_graph.pb'
        net = cv2.dnn_DetectionModel(weights_path, config_file)
        net.setInputSize(320, 320)
        net.setInputScale(1.0 / 127.5)
        net.setInputMean((127.5, 127.5, 127.5))
        net.setInputSwapRB(True)
        font_scale = 3
        font = cv2.FONT_HERSHEY_COMPLEX
        class_index, confidence, bbox = net.detect(img, confThreshold=0.5)

        for ClassInd, conf, boxes in zip(class_index.flatten(), confidence.flatten(), bbox):
            cv2.rectangle(img, boxes, (0, 255, 0), thickness=3)
            cv2.putText(img, CLASSES[ClassInd - 1], (boxes[0] + 10, boxes[1]), font, fontScale=font_scale,
                        color=(0, 0, 255), thickness=3)

        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        st.image(image, caption='Object detection result', use_column_width=True)


@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model("my_model.h5")
    return model


def predict(image, model):
    image = Image.open(image)
    new_image = image.resize((256, 256))
    # st.image(image)
    # image = img_to_array(image)
    new_image = np.asarray(new_image)  # Since our model accepts inputs in the form of tensors
    img_batch = np.expand_dims(new_image, 0)  # Adding fourth dim as model accepts inputs in batch
    predictions = model.predict(img_batch)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]  # finds the index  of max prob amongst CLASSES
    confidence = np.max(predictions[0])

    return predicted_class, confidence


def first_predictor(image):
    # status = st.text("Loading model ...")
    model = load_model()
    # status.text("Loading model ... done!")
    # image = st.file_uploader("")
    if image is not None:
        st.image(image)
        # status.text("")
        button = st.button(label="Classify", key="classify_tab1")
        if button:
            prediction, confidence = predict(image, model)
            col1, col2 = st.columns(2)
            col1.metric("Predicted Class", prediction)
            col2.metric("Confidence", confidence)
            st.checkbox("Use container width", value=False, key="use_container_width")
            df = pd.DataFrame(data=[[prediction, confidence]], columns=['Class', 'Confidence'])
            st.dataframe(df, use_container_width=st.session_state.use_container_width)

            info(prediction)  # Displaying information related to predicted waste recycling process


def second_predictor(image):
    model = load_model()  # Loading our classifier

    if image is not None:
        st.image(image)

        button = st.button(label="Classify", key="classify_tab2")
        if button:
            prediction, confidence = predict(image, model)
            col1, col2 = st.columns(2)
            col1.metric("Predicted Class", prediction)
            col2.metric("Confidence", round(confidence, 2))


def main():
    tab1, tab2 = st.tabs(["Upload", "Use Camera"])  # Creating separate tabs for each Classifiers
    with tab1:
        tab1_image = st.file_uploader("Upload an Image")
        first_predictor(tab1_image)
    with tab2:
        # cam_button = st.button("Open Camera")
        # if cam_button:
        #         st.write("Hello world")
        tab2_image = st.camera_input("Take a picture")
        second_predictor(tab2_image)


with st.sidebar:
    st.header("About")
    st.markdown('An AI system integrated with object detection, Image classification and waste management')
    st.sidebar.title("Prefer your choice")
    app_mode = st.sidebar.selectbox("Choose the app mode",
                                    ["Home", "Real time Object Detection", "Object Detection", "Waste Classification",
                                     "Notify Concerned Authority"])
    st.sidebar.caption("")
    st.markdown("Made by [Sandeep Kashyap](https://www.linkedin.com/in/sandeep-kashyap-aa1545170/)")
    st.header("Resources")
    st.markdown('''
            - [Github](nothing in here)
            - [Streamlit](https://github.com/sandy252)
            ''')

    st.sidebar.header('Deploy')
    st.sidebar.markdown(
        '[Streamlit Community Cloud](https://streamlit.io/cloud)'
        )


if app_mode == "Real time Object Detection":
    st.header("live demo")
    webrtc_streamer(key='example',
                    video_processor_factory=VideoTransformer,
                    rtc_configuration={  # Add this line
                        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
                    }
                    )

if app_mode == "Object Detection":
    st.header("object detection for Images")
    image_ob()

if app_mode == "Waste Classification":
    st.header("Waste Classification")
    main()

if app_mode == "Home":
    st.header("Welcome")
    st.subheader("Use the side bar for various app modes")
    st.markdown(
        "This project demonstrates object detection using camera or phone, waste classification, waste management "
        "system into an interactive Streamlit app.\n\n "
        "Basically there are three app modes available with different feature.\n\n The first app gives a live "
        "demonstration of real time object detection. For now "
        "the model is a pretrained model from tensorflow model zoo but later I will be creating my own model for "
        "custom object detection\n\n "
        "The second performs waste classification with 6 classes.\n\n "
        "People can also participate in waste management by using the third app mode where one can notify concerned "
        "authority by sending a mail along with the image of waste and some other details.")

    st.markdown("""If you have any suggestions, feel free to write to 
                kashyapsandeep252@gmail.com""",
                unsafe_allow_html=True)

if app_mode == "Notify Concerned Authority":
    st.header("Notify Local Municipality")
    notify()

