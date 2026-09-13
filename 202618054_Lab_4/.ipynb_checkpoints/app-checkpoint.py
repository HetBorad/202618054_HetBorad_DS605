import streamlit as st
import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "airbnb_price_model.pkl"))
location_lookup = pd.read_csv(os.path.join(BASE_DIR, "location_lookup.csv"))

st.set_page_config(
    page_title="Airbnb Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 Airbnb Price Prediction")
st.write("Enter the details of an Airbnb listing to estimate its nightly price.")

st.subheader("📍 Location")

neighbourhood_group = st.selectbox(
    "Neighbourhood Group",
    sorted(location_lookup["neighbourhood_group"].unique())
)

neighbourhoods = location_lookup[
    location_lookup["neighbourhood_group"] == neighbourhood_group
]["neighbourhood"].sort_values().tolist()

neighbourhood = st.selectbox(
    "Neighbourhood",
    neighbourhoods
)

location = location_lookup[
    (location_lookup["neighbourhood_group"] == neighbourhood_group) &
    (location_lookup["neighbourhood"] == neighbourhood)
].iloc[0]

latitude = location["latitude"]
longitude = location["longitude"]

st.subheader("🏠 Property Details")

room_type = st.selectbox(
    "Room Type",
    [
        "Entire home/apt",
        "Private room",
        "Shared room"
    ]
)

st.subheader("📊 Listing Details")

minimum_nights = st.number_input(
    "Minimum Nights",
    min_value=1,
    max_value=365,
    value=3,
    step=1
)

number_of_reviews = st.number_input(
    "Number of Reviews",
    min_value=0,
    value=50,
    step=1
)

reviews_per_month = st.number_input(
    "Reviews per Month",
    min_value=0.0,
    value=2.0,
    step=0.1
)

calculated_host_listings_count = st.number_input(
    "Host Listings Count",
    min_value=1,
    value=2,
    step=1
)

availability_365 = st.number_input(
    "Availability (Days per Year)",
    min_value=0,
    max_value=365,
    value=200,
    step=1
)

st.divider()

if st.button("💰 Predict Price", use_container_width=True):

    input_data = pd.DataFrame([{
        "neighbourhood_group": neighbourhood_group,
        "neighbourhood": neighbourhood,
        "latitude": latitude,
        "longitude": longitude,
        "room_type": room_type,
        "minimum_nights": minimum_nights,
        "number_of_reviews": number_of_reviews,
        "reviews_per_month": reviews_per_month,
        "calculated_host_listings_count": calculated_host_listings_count,
        "availability_365": availability_365
    }])

    prediction = model.predict(input_data)[0]

    st.success(
        f"### Estimated Nightly Price: ${prediction:.2f}"
    )