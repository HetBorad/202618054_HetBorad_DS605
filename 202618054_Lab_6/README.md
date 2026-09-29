# DS605: Fundamentals of Machine Learning – Lab Assignment 6

## Student Details

- **Name:** Borad Het Rameshbhai
- **Student ID:** 202618054
- **Course:** DS605 – Fundamentals of Machine Learning
- **Assignment:** Lab Assignment 6
- **Image Dataset:** Asphalt Crack Dataset (Medeley Data)
- **Text Dataset:** Email Spam Classification Dataset (Kaggle)


- **Objective:** Convert raw image and text data into numerical feature representations and use traditional machine-learning models for classification.

---

## **Observations:**

### **Image Dataset:**

- The image dataset contains **400 images**, with **200 Crack** images and **200 Non-Crack** images.
- All images have the same size of **448 × 448 pixels** with 3 color channels.
- The images were converted from BGR to grayscale for feature extraction.
- The grayscale image has pixel values ranging from **0 to 255**.
- Six features were extracted from each image: **mean brightness, contrast, dark pixel ratio, bright pixel ratio, edge count, and edge density**.
- Canny edge detection was used to identify edges in the images.
- The baseline Logistic Regression model achieved:
  - Accuracy = **85.00%**
  - Precision = **81.82%**
  - Recall = **90.00%**
  - F1 Score = **85.71%**
- The Canny thresholds were changed from **(100, 200)** to **(50, 150)**.
- After the change, the accuracy increased from **85.00% to 86.25%** and the F1 score increased from **85.71% to 87.06%**.
- The computation time changed only slightly, so the lower Canny thresholds improved the classification performance without a major increase in computation time.

### **Text Dataset:**

- The email dataset contains **5,172 emails** and **3,000 word-count features**.
- There are **3,672 emails in class 0** and **1,500 emails in class 1**.
- The `Email No.` column was removed because it is only an identifier, while `Prediction` was used as the target variable.
- The dataset provided in `emails.csv` was already in a word-count feature representation, so the 3,000 word columns were used as the input features.
- The baseline Logistic Regression model achieved:
  - Accuracy = **98.26%**
  - Precision = **95.78%**
  - Recall = **98.33%**
  - F1 Score = **97.04%**
- The baseline model took approximately **4.26 seconds** for training and **0.041 seconds** for prediction.
- The number of features was reduced from **3,000 to 1,500** by selecting the most frequent features.
- The reduced-feature model decreased training time from **4.26 seconds to 2.64 seconds** and prediction time from **0.041 seconds to 0.028 seconds**.
- However, accuracy decreased slightly from **98.26% to 97.87%**, and F1 score decreased from **97.04% to 96.37%**.
- Therefore, reducing the number of features reduced computation time but caused a small decrease in classification performance.