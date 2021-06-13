# Core Packages
from managed_db import *
import streamlit as st

# EDA Packages
import pandas as pd
import numpy as np

# Utils
import os
import joblib
import hashlib
# passlib,bcrypt

# Data Viz Pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


def generate_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def verify_hashes(password, hashed_text):
    if generate_hashes(password) == hashed_text:
        return hashed_text
    return False


# Load ML Models
def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), "rb"))
    return loaded_model


def main():
    """Scour Depth Prediction App"""
    st.title("Scour Depth Prediction App")

    menu = ["Home", "Login", "SignUp"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        pass

    elif choice == "Login":
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type='password')

        if st.sidebar.checkbox("Login"):
            create_usertable()
            hashed_password = generate_hashes(password)
            result = login_user(username, verify_hashes(
                password, hashed_password))

            if result:
                st.success("Welcome {}".format(username))

                y_Dp = st.number_input("y/Dp")
                Dp_d50 = st.number_input("Dp/d50")
                Fd = st.number_input("Fd")
                sigma = st.number_input("sigma")
                logT = st.number_input("log(T)")

                feature_list = [y_Dp, Dp_d50, Fd, sigma, logT]
                single_sample = np.array(feature_list).reshape(1, -1)

                model_choice = st.selectbox("Select Model", [
                                            "XGB", "Extra Trees", "Random Forest", "Ada Boost", "MLP", "Lasso", "Bayesian", "Ridge", "Elastic Net"])

                if st.button("Predict"):
                    st.write("Predicted scour depth wrt the diamater is : ")

                    model_path = "./Models/" + model_choice + ".pkl"

                    loaded_model = load_model(model_path)
                    prediction = loaded_model.predict(single_sample)
                    st.write(prediction[0])

            else:
                st.warning("Incorrect Username/Password")

    elif choice == "SignUp":
        new_username = st.text_input("Username")
        new_password = st.text_input("Password", type='password')
        confirm_password = st.text_input("Confirm Password", type='password')

        if new_password == confirm_password:
            st.success("Password Confirmed")
        else:
            st.warning("Passwords are not the same")

        if st.button("Submit"):
            create_usertable()
            hashed_new_password = generate_hashes(new_password)
            add_userdata(new_username, hashed_new_password)
            st.success("You have successfully registered")
            st.info("Login to get started")


# footer = """<style>
# a:link , a:visited{
# color: blue;
# background-color: transparent;
# text-decoration: underline;
# }

# a:hover,  a:active {
# color: red;
# background-color: transparent;
# text-decoration: underline;
# }

# .footer {
# position: fixed;
# left: 0;
# bottom: 0;
# width: 100%;
# background-color: green;
# color: black;
# text-align: center;
# }
# </style>
# <div class="footer">
# <p>Developed with ❤️ by<br><a style='text-align: center;' href="https://github.com/yashsharma8415" target="_blank">Yash Sharma</a> and
# <a style='text-align: center;' href="https://github.com/anishpatil31" target="_blank">Anish Patil</a></p>
# </div>
# """

# st.markdown(footer, unsafe_allow_html=True)


if __name__ == '__main__':
    main()
