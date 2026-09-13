# 🏠 Airbnb Price Prediction

An end-to-end Machine Learning project that predicts the nightly price of Airbnb listings using listing, location, room type, review, and availability information.

## 📌 Project Overview

This project follows a complete Machine Learning workflow:

- Data loading and exploration
- Exploratory Data Analysis (EDA)
- Data cleaning
- Outlier handling
- Feature engineering and selection
- Data preprocessing
- Regression model training
- Model comparison
- Hyperparameter tuning
- Overfitting analysis
- Feature importance analysis
- Model and pipeline saving
- Streamlit web application
- Price prediction using realistic Airbnb listing information

## 🎯 Objective

The main objective is to build a Machine Learning model that can estimate the nightly price of an Airbnb listing based on its characteristics and location.

The final model is integrated into a Streamlit application where users can enter listing details and receive an estimated nightly price.

## 📊 Dataset

The project uses the **New York City Airbnb Open Data (2019)** dataset from Kaggle.

## 🔍 Exploratory Data Analysis

EDA was performed to understand the dataset and identify important patterns.

The analysis included:

- Dataset structure and data types
- Missing value analysis
- Price statistics
- Price distribution
- Price skewness
- Price by room type
- Correlation analysis
- Listings by room type
- Price vs minimum nights
- Price vs number of reviews
- Price vs availability
- Minimum nights distribution
- Reviews per month distribution
- Availability distribution
- Top neighbourhoods by number of listings

## 🤖 Machine Learning Models

The following regression models were trained and compared:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- Extra Trees Regressor
- Tuned Random Forest Regressor
- Random Forest with log-transformed target

## 📈 Model Comparison

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 60.59 | 111.18 | 0.2882 |
| Decision Tree | 71.51 | 140.51 | -0.1369 |
| Random Forest | 55.08 | 104.66 | 0.3692 |
| Gradient Boosting | 56.06 | 106.57 | 0.3460 |
| Extra Trees | 56.10 | 108.11 | 0.3269 |
| **Tuned Random Forest** | **53.31** | **102.64** | **0.3933** |
| Log-target Random Forest | 49.55 | 105.36 | 0.3608 |

## 🏆 Final Model

The **Tuned Random Forest Regressor** was selected as the final model.

It achieved:

- **MAE:** 53.31
- **RMSE:** 102.64
- **R²:** 0.3933

The model was selected because it achieved the best overall combination of RMSE and R².

Although the log-target Random Forest achieved a lower MAE, the Tuned Random Forest achieved better RMSE and R².

## 🔧 Hyperparameter Tuning

`RandomizedSearchCV` with 3-fold cross-validation was used to tune the Random Forest model.

### Best Parameters

```text
n_estimators = 100
max_depth = 30
min_samples_split = 5
min_samples_leaf = 1
max_features = sqrt

## ⚠️ Important Limitations

1. **Model performance:** The final R² score of 0.3933 indicates that the model explains part of the variation in Airbnb prices, but many factors affecting price are not included.

2. **Price capping:** Extreme prices were capped at $1000 to reduce the influence of extreme outliers. Therefore, the model is not designed to accurately predict listings above this value.

3. **Market factors:** Important factors such as seasonality, special events, demand, amenities, and recent market conditions are not included.

4. **Generalization:** Predictions for unusual or very different listings may be less accurate than predictions for listings similar to those present in the training data.

## 📝 Overall Conclusion

The project demonstrates a complete Machine Learning workflow from raw Airbnb data to a working prediction application.

The data was explored and cleaned, relevant features were selected, multiple regression models were compared, and the best model was optimized using hyperparameter tuning.

The final **Tuned Random Forest model achieved an R² score of 0.3933**, with an MAE of **53.31** and RMSE of **102.64**.

The model was successfully integrated into a Streamlit application that allows users to enter Airbnb listing information and receive an estimated nightly price.