# Scour Depth Prediction 

## 📌 Introduction

<h4> A Streamlit web-application which deals with the determination of Scour depth of a bridge based on different aspects of the nature 
which are basically the input parameters for the 9 machine learning regression algorithms that have been used at the backend. </h4>


Many bridge failures occur mostly as a result of scouring around the bridge pier during large floods.
The temporal variation of local pier scour depth is very complex, especially for cases where the bed comprises a sediment mixture.
Many semi-empirical models have been proposed to predict the time-dependent local pier scour depth.
Here, we focus on one such model that takes a combination of various parameters such as approach flow depth, diameter of pier, median grain size of sediment, densimetric particle Froude number, critical densimetric particle Froude number for inception of sediment movement at a pier, sediment non-uniformity parameter and time.
Pier scouring can be defined as a process due to which the particles of the soil or rock around the periphery of the pier of the highway bridge spanning over a water body, gets eroded and removed over a certain depth called scour depth. 
Scouring usually occurs when the velocity of the flowing water increases or crosses the limiting value that the soil particles can easily handle. 
A crossing bridge, with pier and abutments in the river bed and banks, represents an alteration of the natural geometry of the river section and, thereby, creates an obstacle for the river flow that, as it approaches the bridge, has to change its own natural pattern; furthermore, because of the modified flow conditions at the bridge crossing, the streamflow acquires a strong erosive power.

<h4>
This project is designed on the determination of variation of Scour depth of a bridge with respect to various parameters. </h4>

<h3> Key Features </h3>

- Integrated XGB, Extra Trees, Random Forest, Ada Boost, MLP, Lasso, Bayesian, Ridge, Elastic Net regressors.
- Implemented features like entering input variables at the user end, selection of algorithm type to use, etc
- Hosted the project on Streamlit Share




## To run this project

- Clone(fork) this repository
- Run these following commands on your terminal/ cmd prompt:
  - cd Scour-Depth-Prediction
  - pip install streamlit
  - pip install scikit-learn
  - streamlit run app.py
- Wait for few seconds, it will start running on your localhost



## 💥 How to Contribute?
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)



## ⭐ Issues:
For major changes, you are welcome to open an issue to discuss what you would like to change. Enhancements will be appreciated.

<p align = "center">
  
<a href="#"><img src="http://ForTheBadge.com/images/badges/built-by-developers.svg" alt="built by developers"></a>
[![built with love](https://forthebadge.com/images/badges/built-with-love.svg)]

</p>
