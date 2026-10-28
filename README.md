# Customer Segmentation Using K-Means Clustering

## Project Overview

This project applies **K-Means Clustering**, an unsupervised Machine Learning algorithm, to segment mall customers based on their age, annual income, and spending score.

The goal is to identify customer groups with similar characteristics and understand their spending behavior. These segments can help businesses make more informed decisions about customer engagement and marketing strategies.

## Problem Statement

To identify meaningful customer segments from the Mall Customers dataset using K-Means Clustering and interpret the groups based on customer demographics, income, and spending behavior.

## Dataset

- **Dataset Name:** Mall Customers Dataset
- **File Name:** `Mall_Customers.csv`
- **Source:** Kaggle
- **Features Available:** CustomerID, Gender, Age, Annual Income (k$), Spending Score (1-100)

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## Features Used for Clustering

The following numerical features were selected:

- **Age:** The customer's age.
- **Annual Income (k$):** The customer's annual income in thousands of dollars.
- **Spending Score (1-100):** A score representing the customer's spending behavior.

The selected features were scaled before clustering so that differences in their numerical ranges would not unfairly influence the algorithm.

## Project Workflow

1. Load and explore the dataset using Pandas.
2. Select relevant numerical features.
3. Prepare and scale the selected features.
4. Apply the Elbow Method to investigate a suitable number of clusters.
5. Train the K-Means Clustering model.
6. Assign cluster labels to customers.
7. Visualize the clusters using a scatter plot.
8. Analyze the average characteristics of each customer segment.

## Elbow Method

The Elbow Method was used to determine a suitable number of clusters by calculating the within-cluster sum of squares (inertia) for different values of K.

Based on the elbow plot, **4 clusters** were selected for the final model.

## Model Configuration

The K-Means model was configured with the following parameters:

- `n_clusters = 4`
- `random_state = 42`
- `n_init = 10`

The algorithm groups customers according to the similarity of their selected features.

## Cluster Visualization

A scatter plot was created to visualize the customer segments using:

- **X-axis:** Annual Income (k$)
- **Y-axis:** Spending Score (1-100)
- **Colors:** Different cluster assignments

## Cluster Analysis

The following table summarizes the average age, annual income, and spending score for each cluster.

| Cluster | Average Age | Average Income (k$) | Average Spending Score |
|---|---:|---:|---:|
| 0 | 53.98 | 47.71 | 39.97 |
| 1 | 32.88 | 86.10 | 81.53 |
| 2 | 25.44 | 40.00 | 60.30 |
| 3 | 39.37 | 86.50 | 19.58 |

### Understanding the Customer Segments

**Cluster 0 — Older, Moderate-Spending Customers**

These customers are older on average, have comparatively lower annual incomes than the high-income groups, and have moderate spending scores.

**Cluster 1 — High-Income, High-Spending Customers**

These customers have high average annual incomes and high spending scores. They may be a useful segment for studying premium offers and customer loyalty strategies.

**Cluster 2 — Younger, Moderate-Income Customers**

These customers are younger on average, have lower average annual incomes, and show relatively high spending scores compared with their income levels.

**Cluster 3 — High-Income, Low-Spending Customers**

These customers have high average annual incomes but low spending scores. Businesses could investigate whether different products, promotions, or customer experiences might better meet their needs.

*Note: Cluster numbers are labels assigned by the algorithm; they do not represent rankings.*

## What I Learned

Through this project, I learned how to:

- Apply unsupervised Machine Learning to data without predefined target labels.
- Select relevant numerical features for clustering.
- Prepare data and apply feature scaling.
- Use the Elbow Method to choose a suitable number of clusters.
- Train a K-Means model using Scikit-learn.
- Assign cluster labels and visualize customer segments.
- Interpret cluster summaries to understand customer characteristics and spending patterns.

## Conclusion

The project applied K-Means Clustering to divide mall customers into four segments based on age, annual income, and spending score.

The resulting groups illustrate different combinations of customer demographics, income levels, and spending behavior. This demonstrates how clustering can support exploratory customer analysis and help businesses develop more targeted marketing strategies.

## Limitations and Future Improvements

- Compare clustering results using alternative values of K.
- Evaluate clustering quality using metrics such as the Silhouette Score.
- Experiment with different feature combinations.
- Explore customer segmentation using additional behavioral data.
- Build an interactive dashboard to explore the customer groups.

## How to Run the Project

1. Clone or download this repository.
2. Install the required libraries:

   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn jupyter
   ```

3. Ensure `Mall_Customers.csv` is available at the file path used in the notebook.
4. Open the Jupyter Notebook in VS Code or Jupyter Notebook.
5. Run the notebook cells in order.

## Dataset Source

Kaggle — Mall Customers Dataset

## Disclaimer

This project is intended for educational purposes. The customer segments are exploratory groupings based on the selected features and should not be treated as definitive descriptions of individual customers.
