import streamlit as st
import pandas as pd
import numpy as np
import joblib
import xgboost as xgb
import os
import extraction

st.set_page_config(page_title="Phishing Email Detector", layout="centered")

# ----------------------------------------------
# 1. Feature processing pipeline
# ----------------------------------------------
def build_features(subject: str, body: str):
    df = pd.DataFrame([{
        "Subject": subject,
        "Body": body,
        "Label": "Legitimate"
    }])

    df = extraction.clean_data(df)
    df = extraction.feature_extraction(df)
    df = extraction.new_feature(df)

    if "label_value" in df.columns:
        df = df.drop(columns=["label_value"])

    df = df.drop(columns=["Subject", "Body", "Label"])

    return df.select_dtypes(include=[np.number])


# ----------------------------------------------
# 2. Load models dynamically
# ----------------------------------------------
@st.cache_resource
def load_model_email(model_name):

    if model_name == "LightGBM":
        model = joblib.load(r"source_code/lightgbm_model_new.pkl")
        return model, "lightgbm"

    elif model_name == "XGBoost (recommendation)":
        model = xgb.XGBClassifier()
        model.load_model(r"source_code/xgboost_model_add_new_feature.bin")
        return model, "xgboost"

    elif model_name == "voting (SVM+XGBoost)":
        model = joblib.load(r"source_code/voting_classifier_model.pkl")
        return model, "voting"

    else:
        raise ValueError("Model does not exist.")


# ----------------------------------------------
# 3. Predict probability
# ----------------------------------------------
def predict_probability(model, model_type, features):

    proba = model.predict_proba(features)[0][1]
    return float(proba)


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
        ["XGBoost (recommendation)", "voting (SVM+XGBoost)", "LightGBM"]
    )

    submitted = st.form_submit_button("Predict")


if submitted:

    if not subject and not body:
        st.error("❗ Please enter at least a Subject or Body.")
        st.stop()

    # ---------------------------
    # STEP 1: Extracting features
    # ---------------------------
    step_extract = st.empty()
    step_extract.info("🔄 Extracting features...")

    features = build_features(subject, body)

    step_extract.success("✅ Extracting features Done!")


    # ---------------------------
    # STEP 2: Loading model
    # ---------------------------
    step_model = st.empty()
    step_model.info("🔄 Loading model...")

    model, model_type = load_model_email(model_choice)

    step_model.success("✅ Loading model Done!")


    # ---------------------------
    # STEP 3: Making prediction
    # ---------------------------
    step_predict = st.empty()
    step_predict.info("🔄 Making prediction...")

    probability = predict_probability(model, model_type, features)

    step_predict.success("✅ Making prediction Done!")


    # ---------------------------
    # OUTPUT
    # ---------------------------
    st.subheader("Prediction Result")
    st.metric("Phishing Probability", f"{probability*100:.2f}%")

    label = "Phishing" if probability >= 0.5 else "Legitimate"
    st.write(f"**Predicted Label:** {label}")

    with st.expander("🔍 Feature Vector Preview"):
        st.write(features)
