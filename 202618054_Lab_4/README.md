# Airbnb Price Prediction

## Project Overview

This project predicts the estimated nightly price of an Airbnb listing using machine learning.

The project follows an end-to-end machine learning workflow including data cleaning, exploratory data analysis, preprocessing, feature engineering, model training, hyperparameter tuning, evaluation, and deployment using Streamlit.

## Dataset

The dataset used is the New York City Airbnb Open Data from Kaggle.

Dataset: AB_NYC_2019.csv

## Data Preprocessing

The following preprocessing steps were performed:

- Removed listings with zero price.
- Removed unnecessary columns such as name, host_name, and last_review.
- Filled missing reviews_per_month values with 0.
- Checked and handled duplicate records.
- Capped extreme price values at $1000.
- Capped minimum_nights at 365 days.
- Removed identifier columns such as id and host_id.
- Applied median imputation and StandardScaler to numerical features.
- Applied OneHotEncoder to categorical features.

## Features Used

- neighbourhood_group
- neighbourhood
- latitude
- longitude
- room_type
- minimum_nights
- number_of_reviews
- reviews_per_month
- calculated_host_listings_count
- availability_365

## Models Compared

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 60.59 | 111.18 | 0.2882 |
| Decision Tree | 71.51 | 140.51 | -0.1369 |
| Random Forest | 55.08 | 104.66 | 0.3692 |
| Gradient Boosting | 56.06 | 106.57 | 0.3460 |
| Extra Trees | 56.10 | 108.11 | 0.3269 |
| Tuned Random Forest | 53.31 | 102.64 | 0.3933 |
| Log-target Random Forest | 49.55 | 105.36 | 0.3608 |

## Final Model

The Tuned Random Forest model was selected as the final model because it achieved the highest R² score and the lowest RMSE among the tested models.

Final performance:

- MAE: 53.31
- RMSE: 102.64
- R²: 0.3933

## Streamlit Application

A Streamlit web application was created where users can enter Airbnb listing information and receive an estimated nightly price.

The application allows users to select:

- Neighbourhood Group
- Neighbourhood
- Room Type
- Minimum Nights
- Number of Reviews
- Reviews per Month
- Host Listings Count
- Availability

The application automatically determines the approximate latitude and longitude for the selected neighbourhood.

## Project Files

- `DS605_Lab4.ipynb` - Complete machine learning notebook
- `app.py` - Streamlit application
- `airbnb_price_model.pkl` - Trained model pipeline
- `location_lookup.csv` - Neighbourhood and coordinate lookup
- `requirements.txt` - Required Python libraries

## Limitations

- Airbnb prices can vary due to factors not available in the dataset.
- The model explains part of the variation in prices but cannot perfectly predict actual market prices.
- Extreme prices were capped at $1000.
- Latitude and longitude are represented using average coordinates for each neighbourhood in the Streamlit application.

## Conclusion

The project successfully demonstrates an end-to-end machine learning workflow for Airbnb price prediction, from data preprocessing and model comparison to a working Streamlit prediction application.