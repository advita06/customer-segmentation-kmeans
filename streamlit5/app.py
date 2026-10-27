import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("Mall_Customers (1).csv")

# Title
st.title("Customer Segmentation using K-Means")

# 1. Display Dataset
st.header("1. Customer Dataset")
st.dataframe(df)

# Select features
X = df[["Annual Income (k$)", "Spending Score (1-100)"]]

# K-Means model
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)

# Create clusters
df["Cluster"] = kmeans.fit_predict(X)

# 2. Clustering Result
st.header("2. Clustering Results")

cluster_summary = df.groupby("Cluster")[
    ["Age", "Annual Income (k$)", "Spending Score (1-100)"]
].mean()

st.dataframe(cluster_summary)

# 3. Graph
st.header("3. Customer Clusters")

fig, ax = plt.subplots()

ax.scatter(
    df["Annual Income (k$)"],
    df["Spending Score (1-100)"],
    c=df["Cluster"]
)

ax.set_xlabel("Annual Income (k$)")
ax.set_ylabel("Spending Score (1-100)")
ax.set_title("Customer Segments using K-Means")

st.pyplot(fig)