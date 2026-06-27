<h1 align="center">🏠 House Price Prediction System</h1>

<p align="center">
  <img src="logo.jpeg" width="200"/>
</p>

<p align="center">
  A machine learning web application that predicts house prices based on property features using an XGBoost regression model.
</p>

<p align="center">
  <a href="https://house-price-estimator-ai-2026.streamlit.app/">🚀 Live Demo</a> •
  <a href="https://www.kaggle.com/datasets/shree1992/housedata">📊 Dataset</a> •
  <a href="https://www.linkedin.com/in/baqar-ali-0858b0374">👤 LinkedIn</a> •
  <a href="https://github.com/baqar360/House-Price-Prediction">💻 GitHub</a>
</p>

> ⚠️ **Note:** This model is trained on a **Washington State, USA** housing dataset. Predictions are applicable to the US real estate market only.

---

## 📌 Project Overview

This project is a machine learning based house price prediction system. The goal is to predict house prices based on different property features such as bedrooms, bathrooms, living area, location, condition, and other factors. A Streamlit web application was created so users can enter house details and get an estimated price prediction.

---

## ❗ Problem Statement

Many people face difficulty estimating the correct price of a house when buying or selling a property. House prices are often based on guesses, personal opinions, or inaccurate information.

This system solves this problem by using machine learning to estimate house prices based on real property features — providing a quick, reliable, and unbiased price estimate.

---

## 🎯 Objectives

- Build a machine learning model for house price prediction
- Perform data cleaning and feature engineering
- Compare multiple regression algorithms
- Create an easy-to-use prediction interface using Streamlit

---

## 📊 Dataset Overview

| Property | Details |
|---|---|
| Source | [Kaggle – House Price Dataset](https://www.kaggle.com/datasets/shree1992/housedata) |
| Region | Washington State, USA |
| Records | ~4,600 houses |
| Target Variable | `price` (USD) |

**Features used:**

| Feature | Description |
|---|---|
| `bedrooms` | Number of bedrooms |
| `bathrooms` | Number of bathrooms |
| `sqft_living` | Living area in square feet |
| `floors` | Number of floors |
| `waterfront` | Waterfront property or not |
| `view` | View quality rating (0–4) |
| `condition` | Overall condition (1–5) |
| `sqft_above` | Square footage above ground |
| `sqft_basement` | Square footage of basement |
| `street`, `city`, `statezip` | Location information |

---

## 🔍 Exploratory Data Analysis

### Key Findings

- Houses with **0 bedrooms** had unusually high prices and were removed as outliers
- The **price column** contained extreme outliers that were cleaned
- **Waterfront houses** were significantly more expensive than non-waterfront
- **Location (city)** had a strong impact on house prices
- Some features had low contribution to predictions and were removed

---

## ⚙️ Machine Learning Workflow

```
Data Loading → EDA → Data Cleaning → Feature Selection →
Preprocessing → Model Training → Hyperparameter Tuning →
Model Evaluation → Streamlit Deployment
```

---

## 🧪 Model Experiments

Multiple regression models were trained and compared:

| Model | R² Score |
|---|---|
| Linear Regression (Baseline) | ~68% |
| KNN Regression | compared |
| Decision Tree | compared |
| Random Forest | compared |
| Gradient Boosting | compared |
| **XGBoost** ✅ | **~78%** |

---

## 🔧 Feature Engineering & Optimization

| Stage | R² Score |
|---|---|
| Baseline (Linear Regression) | ~68% |
| After feature removal & preprocessing | ~76% |
| After XGBoost + hyperparameter tuning | ~78% |

---

## 🏆 Final Model — XGBoost Regressor

**Why XGBoost was selected:**
- Highest R² score among all tested models
- Better generalization after hyperparameter tuning with `GridSearchCV`
- Handles mixed feature types (numerical + categorical) effectively

**Final Performance:**

| Metric | Value |
|---|---|
| R² Score | ~78% |

---

## 🛠️ Technologies Used

| Tool | Purpose |
|---|---|
| Python | Core language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Scikit-learn | Preprocessing & pipeline |
| XGBoost | Final prediction model |
| Matplotlib & Seaborn | Data visualization |
| Streamlit | Web application |
| Joblib | Model serialization |

---

## 📁 Project Structure

```
House-Price-Prediction/
│
├── app.py                        # Streamlit web application
├── project_model_training.ipynb  # Model training notebook
├── house_price_model.pkl         # Saved XGBoost model
├── logo.jpeg                     # App logo
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## ⚙️ Installation & Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/baqar360/House-Price-Prediction
cd house-price-prediction
```

**2. Create and activate conda environment**
```bash
conda create -n ds_env python=3.10
conda activate ds_env
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the app**
```bash
streamlit run app.py
```

---

## 👤 Author

**Baqar Ali**
Third-year Computer Science Student | Sukkur IBA University

- 🔗 [LinkedIn](https://www.linkedin.com/in/baqar-ali-0858b0374)
- 💻 [GitHub](https://github.com/baqar360/House-Price-Prediction)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
