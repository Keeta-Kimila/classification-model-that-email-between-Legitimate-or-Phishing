# streamlit_app.py
# -------------------------------------------------------------
# Email phishing detection app using extraction.py feature logic
# -------------------------------------------------------------

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import xgboost as xgb
import os

import extraction   # <- your provided extraction.py

st.set_page_config(page_title="Phishing Email Detector", layout="centered")

# ----------------------------------------------
# 1. Feature processing pipeline (uses extraction.py)
# ----------------------------------------------
def build_features(subject: str, body: str):
    """
    Build a full feature row using the 3 required functions:
    1. clean_data
    2. feature_extraction
    3. new_feature
    """

    # Create DataFrame to match training format
    df = pd.DataFrame([{
        "Subject": subject,
        "Body": body,
        "Label": "Legitimate"   # placeholder (required in extraction.feature_extraction)
    }])

    # 1. Clean data
    df = extraction.clean_data(df)

    # 2. Original feature extraction
    df = extraction.feature_extraction(df)

    # 3. New features
    df = extraction.new_feature(df)

    # Remove unused label_value column (model doesn’t use it)
    if "label_value" in df.columns:
        df = df.drop(columns=["label_value"])
        df = df.drop(columns=["Subject"])
        df = df.drop(columns=["Body"])
        df = df.drop(columns=["Label"])

    # Convert to numeric features only
    numeric_df = df.select_dtypes(include=[np.number])

    return numeric_df


# ----------------------------------------------
# 2. Load models dynamically
# ----------------------------------------------
@st.cache_resource
def load_model_email(model_name):

    if model_name == "lightgbm_model_new.pkl":
        model = joblib.load(model_name)
        return model, "lightgbm"

    elif model_name == "xgboost_model_add_new_feature.bin":
        model = xgb.XGBClassifier()
        model.load_model(model_name)
        return model, "xgboost"

    else:
        raise ValueError("Model does not exist.")


# ----------------------------------------------
# 3. Predict probability wrapper
# ----------------------------------------------
def predict_probability(model, model_type, features):

    if model_type == "lightgbm":
        proba = model.predict_proba(features)[0][1]   # class 1 probability
        return float(proba)

    elif model_type == "xgboost":
        proba = model.predict_proba(features)[0][1]
        return float(proba)

    else:
        raise ValueError("Invalid model type.")


# ----------------------------------------------
# Streamlit UI
# ----------------------------------------------
st.title("📧 Email Phishing Detector")
st.write("Enter email Subject & Body, choose a model, and get phishing probability.")

with st.form("input_form"):
    subject = st.text_input("Subject")
    body = st.text_area("Body", height=200)

    model_choice = st.radio(
        "Select Model",
        ["lightgbm_model_new.pkl", "xgboost_model_add_new_feature.bin"]
    )

    submitted = st.form_submit_button("Predict")


if submitted:

    if not subject and not body:
        st.error("❗ Please enter at least a Subject or Body.")
        st.stop()

    st.info("🔄 Extracting features...")

    features = build_features(subject, body)

    st.info("🔄 Loading model...")

    model, model_type = load_model_email(model_choice)

    st.info("🔄 Making prediction...")
    probability = predict_probability(model, model_type, features)

    label = "Phishing" if probability >= 0.5 else "Legitimate"

    st.subheader("Prediction Result")
    st.metric("Phishing Probability", f"{probability*100:.2f}%")
    st.write(f"**Predicted Label:** {label}")

    with st.expander("🔍 Feature Vector Preview"):
        st.write(features)


