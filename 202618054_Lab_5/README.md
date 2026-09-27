# DS605: Fundamentals of Machine Learning – Lab Assignment 5

## Student Details

- **Name:** Borad Het Rameshbhai
- **Student ID:** 202618054
- **Course:** DS605 – Fundamentals of Machine Learning
- **Assignment:** Lab Assignment 5
- **Dataset:** UCI Productivity Prediction of Garments Employee (graments_worker_productivity.csv)


- **Objective:** Build regression and classification models with Scikit-learn, recreate the same workflow manually using only
NumPy and Pandas, and compare predictive performance, execution time, and implementation efficiency.

---

## **Observations:**

### **1. Linear Regression:**

#### The manual Linear Regression model produced the same RMSE as the Scikit-learn model (0.149351). This shows that the manually implemented normal equation produced equivalent results.

#### Feature selection was tested by removing features with smaller coefficient magnitudes. However, the RMSE increased from 0.149351 to 0.150448 after removing features. Therefore, the full 36-feature model was retained.

### **2. Logistic Regression:**

#### The initial manual Logistic Regression model achieved an F1 score of 0.850962.

#### Different learning rates were tested. Increasing the learning rate from 0.01 to 0.1 improved the F1 score to 0.862245 while keeping the number of iterations at 1000.

#### The number of iterations was also tested. Increasing the iterations beyond 1000 did not improve the F1 score, so 1000 iterations was retained.

#### Therefore, the optimized manual Logistic Regression used:

#### - Learning rate = 0.1
#### - Iterations = 1000
#### - F1 Score = 0.862245

### **3. Runtime Comparison:**

#### The manual Linear Regression training time (0.015052 s) was close to the Scikit-learn training time (0.014329 s).

#### The manual Logistic Regression training time was higher than Scikit-learn because the manual implementation uses gradient descent and performs multiple iterations explicitly.

#### The optimized manual Logistic Regression took 0.050110 s for training. Its prediction time was 0.000193 s, compared with 0.000544 s for Scikit-learn.

#### Runtime differences can depend on the implementation, vectorization, library optimizations, and system conditions.

### **4. Overall Observation:**

### The experiment shows that machine learning algorithms can be implemented using NumPy and Pandas without using ready-made machine learning algorithms.

#### The manual Linear Regression implementation matched Scikit-learn closely. Optimization of the manual Logistic Regression through learning-rate tuning improved its F1 score from 0.850962 to 0.862245.

#### Vectorized NumPy operations were used throughout the manual implementation to improve computational efficiency.