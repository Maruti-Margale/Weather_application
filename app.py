import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# --- Data Generation and Model Training (to make the app self-contained) ---
# In a real-world scenario, this model would be loaded from a pre-trained file.
# This section ensures the app is fully functional and does not require a .pkl file.

# Create a simple synthetic dataset for demonstration
np.random.seed(0)
# Features: Age, BMI, Smoker (1=Yes, 0=No)
X = np.array([
    [25, 22.5, 0],
    [35, 28.0, 1],
    [45, 30.2, 1],
    [55, 25.1, 0],
    [20, 20.0, 0],
    [60, 35.0, 1],
    [30, 29.5, 0],
    [40, 24.3, 1],
    [50, 32.1, 0],
    [28, 26.7, 1]
])

# Target variable (charges) with a linear relationship and some noise
# Formula: charges = 150 * age + 350 * bmi + 25000 * smoker + random_noise
y = 150 * X[:, 0] + 350 * X[:, 1] + 25000 * X[:, 2] + np.random.normal(0, 5000, 10)

# Train a simple Linear Regression model on the synthetic data
model = LinearRegression()
model.fit(X, y)

# --- Streamlit App UI and Logic ---
# Set up the Streamlit app page configuration
st.set_page_config(page_title="Insurance Charge Predictor", layout="centered")

# App title
st.title("💰 Insurance Charges Prediction")

# Create the navigation menu in the sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Predict Charges", "About"])

# Display content based on the selected page
if page == "Predict Charges":
    st.markdown("Predict insurance charges based on Age, BMI, and Smoking status.")
    st.markdown("This app uses a simple linear regression model for demonstration.")

    # Input fields for user data
    age = st.slider("Enter Age", min_value=18, max_value=100, value=30)
    bmi = st.number_input("Enter BMI", min_value=10.0, max_value=50.0, value=25.0, step=0.1)
    smoker = st.radio("Do you smoke?", ["Yes", "No"])

    # Convert smoker status to the binary format the model expects
    smoker_val = 1 if smoker == "Yes" else 0

    # Predict button
    if st.button("Predict Charges", use_container_width=True):
        # Prepare the input data as a NumPy array with the correct shape
        input_data = np.array([[age, bmi, smoker_val]])

        # Make the prediction using the trained model
        prediction = model.predict(input_data)[0]

        # Display the formatted result
        st.success(f"💵 Predicted Insurance Charges: ${prediction:,.2f}")

elif page == "About":
    st.header("About This Application")
    st.markdown("""
    This is a simple demo application that predicts insurance charges using a basic machine learning model.
    The model is a **Linear Regression** model trained on a synthetic dataset. It considers three main factors:
    - **Age**: The user's age.
    - **BMI**: Body Mass Index, a measure of body fat.
    - **Smoking Status**: Whether the user is a smoker or not.

    **Disclaimer:** This is for demonstration purposes only and should not be used for actual financial or health advice.
    """)
