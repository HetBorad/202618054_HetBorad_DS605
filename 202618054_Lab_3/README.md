# DS605: Fundamentals of Machine Learning – Lab Assignment 3

## Student Details

- **Name:** Borad Het Rameshbhai
- **Student ID:** 202618054
- **Course:** DS605 – Fundamentals of Machine Learning
- **Assignment:** Lab Assignment 3
- **Dataset:** Kaggle Hotel Booking Demand (hotel_bookings.csv)


- **Objective:** Build and compare Scikit-learn preprocessing pipelines and evaluate two classification models.


---

## Observations

1. The best overall result based on the testing accuracy and F1-Score is given by Decision Tree with Standard Scaler.

2. While comparing f1-score, StandardScaler performs slightly better than MinMaxScaler for Logistic Regression.

3. Scaling makes very little difference for the Decision Tree as a f1-score is not varied by much after applying scaling.

4. Logistic Regression does not show much overfitting due to smaller difference between training and testing accuracy, indicating more stable generalization.

5. The Decision Tree shows possible overfitting because its training accuracy is 99% while its testing accuracy is approximately 85%. The large difference between training and testing performance suggests that the tree fits the training data very closely.