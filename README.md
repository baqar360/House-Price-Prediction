<h1 align="center">House Price Prediction System</h1>

<p align="center">
<img src="logo.png" width="200">
</p>

---

## Project Overview

This project is a machine learning based house price prediction system.
The goal is to predict house prices based on different property features
such as bedrooms, bathrooms, living area, location, condition, and other factors.

A Streamlit web application was created so users can enter house details
and get an estimated price prediction.

---

# Problem Statement

Many people face difficulty estimating the correct price of a house when
buying or selling a property. House prices are often based on guesses,
personal opinions, or inaccurate information.

This system solves this problem by using machine learning to estimate house
prices based on property features.

---

# Objectives

- Build a machine learning model for house price prediction
- Perform data cleaning and feature engineering
- Compare multiple regression algorithms
- Create an easy-to-use prediction interface using Streamlit

---

# Dataset Overview

The dataset contains house-related information including:

- Bedrooms
- Bathrooms
- Living area
- Floors
- Waterfront
- View
- Condition
- Location information

The target variable is:

- Price

---

# Machine Learning Workflow

The project follows these steps:

1. Data loading
2. Exploratory Data Analysis
3. Data cleaning
4. Feature selection
5. Data preprocessing
6. Model training
7. Hyperparameter tuning
8. Model evaluation
9. Deployment using Streamlit

---

# Exploratory Data Analysis (EDA)

## Important Findings

- Houses with 0 bedrooms had unusual high prices and were removed.
- Price column contained extreme outliers.
- Waterfront houses were significantly more expensive.
- Location had a strong impact on house prices.
- Some features had low contribution and were removed.

---

# Model Experiments

Different regression models were tested:

- Linear Regression
- KNN Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- XGBoost


## Baseline Model

Linear Regression was used as the baseline model.

Performance:

R² Score: 68%

---

# Feature Engineering and Optimization

After removing unnecessary features and improving preprocessing:

- Linear Regression improved to approximately 76% R² score.

After hyperparameter tuning:

- XGBoost achieved approximately 78% R² score.

---

# Final Model

The final selected model:

## XGBoost Regressor

Reason:

- Highest R² score
- Better prediction performance
- Improved after optimization


Final Performance:

R² Score: ~78%

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Matplotlib
- Seaborn

---

# Project Structure
