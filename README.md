# 🏠 House Price Prediction System
## 📌 Project Overview
This project is a Machine Learning web application that predicts the price of a house based on different features such as area, number of bedrooms, bathrooms, parking, and other facilities.

The system uses a trained machine learning model to estimate the house price when the user enters the property details through a web interface.

This project demonstrates how machine learning can be integrated with a web application to solve real-world problems.

## 🎯 Objective
The main objective of this project is to:

Predict house prices using machine learning

Build a simple web interface for user input

Demonstrate the use of data preprocessing and model training

Integrate a trained model with a web application using Flask

## 📊 Dataset Features
The dataset used in this project contains the following attributes:

price – Price of the house (target variable)

area – Area of the house in square feet

bedrooms – Number of bedrooms

bathrooms – Number of bathrooms

stories – Number of floors

mainroad – Whether the house is connected to the main road

guestroom – Availability of guest room

basement – Availability of basement

hotwaterheating – Availability of hot water heating

airconditioning – Availability of air conditioning

parking – Number of parking spaces

prefarea – Whether the house is located in a preferred area

furnishingstatus – Furnishing status of the house

## 🧠 Technologies Used
This project uses the following technologies:

Python

Machine Learning (Scikit-Learn)

Flask (Web Framework)

HTML

CSS

Pandas & NumPy

Joblib (Model Saving)

## ⚙️ Project Workflow
The project follows these steps:

Data Collection
The dataset containing house information is collected.

Data Preprocessing
Categorical values like yes/no are converted into numerical values.

Model Training
A machine learning model is trained using the dataset.

Model Saving
The trained model is saved as a .pkl file.

Web Application
A Flask web application is created where users can enter house details.

Prediction
The trained model predicts the house price based on user input.


## 🚀 How to Run the Project
Step 1 – Install required libraries
pip install pandas numpy scikit-learn flask joblib

Step 2 – Train the model
python train_model.py
This will create the trained model file in the models folder.

Step 3 – Run the web application
python app.py

Step 4 – Open in browser
http://127.0.0.1:5000
Enter the house details and click Predict Price to see the estimated house price.

## 📈 Future Improvements
This project can be improved by:

Using advanced models like Random Forest or Gradient Boosting

Adding data visualization dashboards

Deploying the application online

Improving the user interface design

## 👥 Team Project
This project was developed as part of a team-based machine learning project, where my team members worked on:

Data preprocessing

Model development

Web interface design

Integration and testing

## 📌 Conclusion
The House Price Prediction system shows how machine learning and web technologies can be combined to build an intelligent application that helps estimate property prices quickly and efficiently.
