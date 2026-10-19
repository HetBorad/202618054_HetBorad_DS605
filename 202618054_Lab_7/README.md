# DS605: Fundamentals of Machine Learning – Lab Assignment 7

## Student Details

- **Name:** Borad Het Rameshbhai
- **Student ID:** 202618054
- **Course:** DS605 – Fundamentals of Machine Learning
- **Assignment:** Lab Assignment 7
- **Dataset:** AT&T Database of Faces (ORL)

- **Objective:** Represent images numerically, reduce their dimensionality using PCA/eigenfaces, perform face matching in the reduced space, and compare the result with traditional machine-learning classifiers.

---

## **Observations:**

1. **Dimensionality reduction:** Each image originally contains 10,304 pixel features. PCA reduces this to 98 components while retaining approximately 90.06% of the variance.

2. **Explained variance:** The first principal component captures about 17.94% of the variance. More components are required to capture additional facial variation.

3. **Eigenfaces:** The eigenfaces represent major patterns of variation in facial images, including changes in facial structure and appearance.

4. **Image reconstruction:** Reconstructing an image from 98 components produces a recognizable approximation, but some details are lost. The observed reconstruction MSE is approximately 307.40.

5. **Recognition performance:** Raw-pixel nearest-neighbor matching achieved 100% accuracy, while PCA nearest-neighbor matching achieved 95%. Information discarded during PCA may affect recognition performance.

6. **Classifier comparison:** KNN achieved 95% accuracy and linear SVM achieved 97.5% using PCA features. SVM performed better than the PCA nearest-neighbor baseline on this split.

7. **Effect of component count:** With 50 components, SVM achieved 97.5% accuracy while retaining 82.48% of the variance. With 98 components, it achieved the same accuracy while retaining 90.06% of the variance.

8. **Storage reduction:** The original pixel arrays require approximately 4,025 KB, compared with 306.25 KB for the PCA feature arrays. This represents a 92.39% reduction in feature-array storage, excluding the mean face, eigenfaces, labels, and file overhead.

9. **SVD and eigendecomposition:** The largest eigenvalues obtained from SVD and covariance eigendecomposition closely agree. The maximum absolute difference was approximately 8.34e-07.

10. **Overall finding:** PCA substantially reduces dimensionality and storage requirements while preserving useful information for face recognition. The best method depends on the balance between compression and recognition accuracy.

11. **Principal-direction comparison:** The first 10 principal directions obtained using covariance eigendecomposition and SVD had an absolute direction similarity of 1.0 for every component. This confirms that both methods produced aligned principal directions. The comparison results are saved in `outputs/tables/direction_comparison.csv`.

### PCA Component Comparison

| Components | Variance Retained | Feature Reduction | Nearest Neighbor Accuracy | SVM Accuracy |
|---:|---:|---:|---:|---:|
| 20 | 70.49% | 99.81% | 95.00% | 95.00% |
| 50 | 82.48% | 99.51% | 96.25% | 97.50% |
| 98 | 90.06% | 99.05% | 95.00% | 97.50% |
| 150 | 94.31% | 98.54% | 95.00% | 97.50% |