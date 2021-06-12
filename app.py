# Core Pkgs hain yeh
import streamlit as st 

# EDA Pkgs
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

#DB
from managed_db import *
def generate_hashes(password) :
	return hashlib.sha256(str.encode(password)).hexdigest()

def verify_hashes(password, hashed_text) :
	if generate_hashes(password) == hashed_text :
		return hashed_text
	return False


# Load ML Models
def load_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
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
		password = st.sidebar.text_input("Password", type = 'password')

		if st.sidebar.checkbox("Login"):
			create_usertable()
			hashed_pswd = generate_hashes(password)
			result = login_user(username, verify_hashes(password, hashed_pswd))
			if result:
				st.success("Welcome {}".format(username))
			    #st.subheader("Input Parameters")
				#X = df[['y/Dp', 'Dp/d50', 'Fd', 'sigma', 'log(T)']].values
				y_Dp = st.number_input("y/Dp")
				Dp_d50 = st.number_input("Dp/d50")
				Fd = st.number_input("Fd")
				sigma = st.number_input("sigma")
				logT = st.number_input("log(T)")

				feature_list = [y_Dp, Dp_d50, Fd, sigma, logT]
				single_sample = np.array(feature_list).reshape(1,-1)

				model_choice = st.selectbox("Select Model",["XGB","Extra Trees","Random Forest", "Ada Boost", "MLP", "Lasso", "Bayesian", "Ridge", "Elastic Net"])
				if st.button("Predict"):
					st.write("Predicted scour depth wrt the diamater is : ")
					if model_choice == "XGB":
						loaded_model = load_model("XGB.pkl")
						prediction = loaded_model.predict(single_sample)
						st.write(prediction[0])
					elif model_choice == "Extra Trees":
						loaded_model = load_model("Extra_trees.pkl")
						prediction = loaded_model.predict(single_sample)
						st.write(prediction[0])
					elif model_choice == "Random Forest":
						loaded_model = load_model("Random_forest.pkl")
						prediction = loaded_model.predict(single_sample)
						st.write(prediction[0])
					elif model_choice == "Ada Boost":
						loaded_model = load_model("Ada_Boost.pkl")
						prediction = loaded_model.predict(single_sample)
						st.write(prediction[0])
					elif model_choice == "MLP":
						loaded_model = load_model("MLP.pkl")
						prediction = loaded_model.predict(single_sample)
						st.write(prediction[0])
					elif model_choice == "Lasso":
						loaded_model = load_model("Lasso.pkl")
						prediction = loaded_model.predict(single_sample)
						st.write(prediction[0])
					elif model_choice == "Bayesian":
						loaded_model = load_model("Bayesian.pkl")
						prediction = loaded_model.predict(single_sample)
						st.write(prediction[0])
					elif model_choice == "Ridge":
						loaded_model = load_model("Ridge.pkl")
						prediction = loaded_model.predict(single_sample)
						st.write(prediction[0])
					elif model_choice == "Elastic Net":
						loaded_model = load_model("Elastic_Net.pkl")
						prediction = loaded_model.predict(single_sample)
						st.write(prediction[0])
			else:
				st.warning("Incorrect Username/Password"),
	elif choice == "SignUp":
		new_username = st.text_input("Username" )
		new_password = st.text_input("Password",type='password' )

		confirm_password= st.text_input("Confirm Password",type='password' )
		if new_password == confirm_password :
			st.success("Password Confirmed")
		else :
			st.warning("Passwords are not the same")
		
		if st.button("Submit") :
			create_usertable()
			hashed_new_password = generate_hashes(new_password)
			add_userdata(new_username, hashed_new_password) 
			st.success("You have successfully registered")
			st.info("Login to get started")

if __name__ == '__main__':
	main()