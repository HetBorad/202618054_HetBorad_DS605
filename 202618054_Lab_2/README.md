# DS605: Fundamentals of Machine Learning – Lab Assignment 2

## Student Details

- **Name:** Borad Het Rameshbhai
- **Student ID:** 202618054
- **Course:** DS605 – Fundamentals of Machine Learning
- **Assignment:** Lab Assignment 2
- **Dataset:** Kaggle Titanic Dataset (`train.csv`)

- **Objective:** Practice vectorized NumPy operations and basic data wrangling with Pandas using the Titanic dataset.

---

## Observations

1. Female passengers had a considerably higher survival rate (74.20%) than male passengers (18.89%).

2. Female first-class passengers had the highest survival rate (96.81%), whereas male third-class passengers had the lowest (13.54%).

3. Survival rates generally decreased with increasing Pclass, indicating a strong association between passenger class and survival.

4. The Fare column contained 116 outliers according to the 1.5 × IQR rule, with an upper outlier boundary of approximately 65.63.

5. Pclass and Fare showed a negative correlation, as higher passenger-class numbers generally corresponded to lower fares.

6. The Age vs Fare scatter plot showed that most passengers paid relatively low fares, while high-fare passengers were comparatively fewer and included a larger proportion of survivors.

7. The engineered FamilySize and IsAlone features provide additional information about passengers' travelling groups and can be useful for further analysis.