import streamlit as st
import pandas as pd
import joblib


# Page settings
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)


# Load model
model = joblib.load("house_price_model.pkl")


# Sidebar
with st.sidebar:

    st.image("logo.jpeg", width=150)

    st.title("About")

    st.write(
        """
        This application predicts house prices
        using a machine learning model.

        Enter house details and get an estimated price.
        """
    )


# Main area

col_logo, col_title = st.columns([1,4])


with col_logo:
    st.image("logo.jpeg", width=120)


with col_title:
    st.title("🏠 House Price Prediction System")
    st.write(
        "Enter house details below to estimate the price."
    )


st.divider()



# House Information

st.header("🏡 House Information")


col1, col2, col3 = st.columns(3)


with col1:

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=0,
        value=3
    )


    bathrooms = st.number_input(
        "Bathrooms",
        min_value=0.0,
        value=2.0
    )


    floors = st.number_input(
        "Floors",
        min_value=0.0,
        value=1.0
    )



with col2:

    sqft_living = st.number_input(
        "Living Area (sqft)",
        min_value=0,
        value=1500
    )


    sqft_above = st.number_input(
        "Sqft Above",
        min_value=0,
        value=1500
    )


    sqft_basement = st.number_input(
        "Sqft Basement",
        min_value=0,
        value=0
    )



with col3:

    waterfront = st.selectbox(
        "Waterfront",
        [0,1]
    )


    view = st.number_input(
        "View",
        min_value=0,
        value=0
    )


    condition = st.selectbox(
        "Condition",
        [1,2,3,4,5]
    )



# Location

st.header("📍 Location")


col4, col5, col6 = st.columns(3)


with col4:

    street = st.text_input("Street")


with col5:

    city = st.text_input("City")


with col6:

    statezip = st.text_input("State Zip")



country = st.text_input(
    "Country",
    value="USA"
)



st.divider()



# Prediction

if st.button(
    "🔮 Predict House Price",
    use_container_width=True
):

    input_data = pd.DataFrame({

        "bedrooms":[bedrooms],

        "bathrooms":[bathrooms],

        "sqft_living":[sqft_living],

        "floors":[floors],

        "waterfront":[waterfront],

        "view":[view],

        "condition":[condition],

        "sqft_above":[sqft_above],

        "sqft_basement":[sqft_basement],

        "street":[street],

        "city":[city],

        "statezip":[statezip],

        "country":[country]

    })


    prediction = model.predict(input_data)


    st.success("Prediction Completed")


    st.metric(
        "Estimated House Price",
        f"${prediction[0]:,.0f}"
    )