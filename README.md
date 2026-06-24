# Shopper Spectrum: Customer Segmentation and Product Recommendation

This project is an e-commerce analytics application that performs customer segmentation and product recommendation.

## Project Overview

The project analyzes online retail transaction data to understand customer purchase behavior. It uses RFM analysis for customer segmentation and collaborative filtering for product recommendations.

## Features

- Customer segmentation using Recency, Frequency, and Monetary values
- K-Means clustering for customer grouping
- Product recommendation using item-based collaborative filtering
- Streamlit web application with interactive user input

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

## Streamlit App Modules

### 1. Product Recommendation

The user enters a product name, and the app recommends 5 similar products.

### 2. Customer Segmentation

The user enters:

- Recency
- Frequency
- Monetary value

The app predicts the customer segment:

- High-Value
- Regular
- Occasional
- At-Risk

## Files in Repository

- `app.py` : Main Streamlit application
- `recommendations.pkl` : Product recommendation file
- `kmeans_model.pkl` : Trained K-Means clustering model
- `scaler.pkl` : StandardScaler object
- `requirements.txt` : Required Python libraries

## How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
