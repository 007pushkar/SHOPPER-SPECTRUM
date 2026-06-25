import streamlit as st
import pandas as pd
import joblib

# Load models
kmeans_model = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")
recommendations = joblib.load("recommendations.pkl")

# Cluster labels
cluster_mapping = {
    0: "High-Value",
    1: "Regular",
    2: "Occasional",
    3: "At-Risk"
}

# Page setup
st.set_page_config(
    page_title="Shopper Spectrum",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 Shopper Spectrum")
st.subheader("Customer Segmentation and Product Recommendation System")

st.markdown("""
This app provides:
- Product recommendations using collaborative filtering
- Customer segmentation using RFM-based clustering
""")

# Sidebar
option = st.sidebar.selectbox(
    "Choose Module",
    ["Product Recommendation", "Customer Segmentation"]
)

# Recommendation Function
def recommend_products(product_name, recommendations):
    product_name = product_name.upper()

    for product in recommendations.keys():
        if product_name in product.upper():
            return product, recommendations[product]

    return None

    recommendations = (
        similarity_df[matched_product]
        .sort_values(ascending=False)
        .iloc[1:top_n + 1]
        .index
        .tolist()
    )

    return matched_product, recommendations


# Module 1
if option == "Product Recommendation":

    st.header("🎯 Product Recommendation Module")

    product_name = st.text_input("Enter Product Name")

    if st.button("Get Recommendations"):
        if product_name.strip() == "":
            st.warning("Please enter a product name.")
        else:
            result = recommend_products(product_name, recommendations)

            if result is None:
                st.error("Product not found. Try another product name.")
            else:
                matched_product, recommendations = result

                st.success(f"Similar products for: {matched_product}")

                for i, product in enumerate(recommendations, 1):
                    st.markdown(f"### {i}. {product}")


# Module 2
elif option == "Customer Segmentation":

    st.header("👤 Customer Segmentation Module")

    recency = st.number_input(
        "Recency - Days since last purchase",
        min_value=0,
        value=30
    )

    frequency = st.number_input(
        "Frequency - Number of purchases",
        min_value=1,
        value=5
    )

    monetary = st.number_input(
        "Monetary - Total amount spent",
        min_value=0.0,
        value=500.0
    )

    if st.button("Predict Cluster"):
        input_data = pd.DataFrame({
            "Recency": [recency],
            "Frequency": [frequency],
            "Monetary": [monetary]
        })

        scaled_data = scaler.transform(input_data)

        cluster = kmeans_model.predict(scaled_data)[0]

        segment = cluster_mapping.get(cluster, "Unknown Segment")

        st.success(f"Predicted Customer Segment: {segment}")

        st.info(f"Cluster Number: {cluster}")
