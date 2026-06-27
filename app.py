import streamlit as st
import pandas as pd
import joblib

# ── Page settings ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# ── Load model ─────────────────────────────────────────────────────────────────
model = joblib.load("house_price_model.pkl")

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.image("logo.jpeg", width=150)
    st.title("About")
    st.write(
        """
        This application predicts house prices
        using an XGBoost machine learning model.

        Enter house details and get an estimated price.
        """
    )
    st.divider()
    st.caption("⚠️ Trained on Washington State, USA housing data only.")

# ── Header ─────────────────────────────────────────────────────────────────────
col_logo, col_title = st.columns([1, 4])

with col_logo:
    st.image("logo.jpeg", width=120)

with col_title:
    st.title("🏠 House Price Prediction System")
    st.write("Enter house details below to estimate the price.")
    st.caption("⚠️ This model is trained on Washington State, USA data. Predictions may not apply to other regions.")

st.divider()

# ── House Information ──────────────────────────────────────────────────────────
st.header("🏡 House Information")

col1, col2, col3 = st.columns(3)

with col1:
    bedrooms = st.number_input("Bedrooms", min_value=1, max_value=15, value=3)
    bathrooms = st.number_input("Bathrooms", min_value=0.25, max_value=10.0, step=0.25, value=2.0)
    floors = st.number_input("Floors", min_value=1.0, max_value=5.0, step=0.5, value=1.0)

with col2:
    sqft_living = st.number_input("Living Area (sqft)", min_value=100, max_value=15000, value=1500)
    sqft_above = st.number_input("Sqft Above Ground", min_value=100, max_value=15000, value=1500)
    sqft_basement = st.number_input("Sqft Basement", min_value=0, max_value=5000, value=0)

with col3:
    waterfront_input = st.selectbox("Waterfront View", ["No", "Yes"])
    waterfront = 1 if waterfront_input == "Yes" else 0
    view = st.selectbox("View Quality (0=None, 4=Excellent)", [0, 1, 2, 3, 4])
    condition = st.selectbox("Condition (1=Poor, 5=Excellent)", [1, 2, 3, 4, 5])

# ── Location ───────────────────────────────────────────────────────────────────
st.header("📍 Location")

col4, col5, col6 = st.columns(3)

with col4:
    street = st.text_input("Street", placeholder="e.g. 123 Main St")

with col5:
    city = st.text_input("City", placeholder="e.g. Seattle")

with col6:
    statezip = st.text_input("State Zip", placeholder="e.g. WA 98101")

# country is hardcoded as "USA" — model expects it but user doesn't need to enter it

st.divider()

# ── Prediction ─────────────────────────────────────────────────────────────────
if st.button("🔮 Predict House Price", use_container_width=True):

    # Check 1: Empty fields
    if not street.strip() or not city.strip() or not statezip.strip():
        st.warning("⚠️ Please fill in all location fields (Street, City, State Zip).")

    # Check 2: City should not contain numbers
    elif any(char.isdigit() for char in city):
        st.warning("⚠️ City name should not contain numbers. Example: Seattle")

    # Check 3: Street should contain at least one number
    elif not any(char.isdigit() for char in street):
        st.warning("⚠️ Street should include a house number. Example: 123 Main St")

    else:
        input_data = pd.DataFrame({
            "bedrooms":      [bedrooms],
            "bathrooms":     [bathrooms],
            "sqft_living":   [sqft_living],
            "floors":        [floors],
            "waterfront":    [waterfront],
            "view":          [view],
            "condition":     [condition],
            "sqft_above":    [sqft_above],
            "sqft_basement": [sqft_basement],
            "street":        [street.strip()],
            "city":          [city.strip()],
            "statezip":      [statezip.strip()],
            "country":       ["USA"],  # hardcoded — model was trained on USA data only
        })

        prediction = model.predict(input_data)
        price = prediction[0]

        st.success("✅ Prediction Completed")

        st.metric(
            label="Estimated House Price",
            value=f"${price:,.0f}"
        )

        # Warn if prediction exceeds training data range
        if price > 3_400_000:
            st.warning(
                "⚠️ This prediction exceeds the training data range ($3.4M). "
                "The result may be unreliable."
            )

        # Show input summary
        with st.expander("📋 View Input Summary"):
            st.dataframe(input_data)
