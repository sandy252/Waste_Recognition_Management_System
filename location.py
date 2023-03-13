import streamlit as st

st.header("Welcome")

st.markdown("This project demonstrates object detection using camera or phone, waste classification, waste management "
            "system into an interactive Streamlit app.\n\n "
            "Basically there are three app modes available with different feature.\n\n The first app gives a live "
            "demonstration of real time object detection. For now "
            "the model is a pretrained model from tensorflow model zoo but later I will be creating my own model for "
            "custom object deteciton\n\n "
            "The second performs waste classification with 6 classes. "
            "People can also participate in waste management by using the third app mode where one can notify "
            "concerned authority using by sending a mail along with the image of waste and some other details like "
            "location.")

st.markdown("""If you have any suggestions, feel free to write to  <span>style='color:red'>kashyapsandeep252@gmail.com</span>
               """,
            unsafe_allow_html=True)
