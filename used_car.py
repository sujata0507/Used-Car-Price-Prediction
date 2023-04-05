import streamlit as st
import requests
import joblib
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

model = joblib.load("C:/Users/pga28/PycharmProject/USed_Car_price/model.pkl")
standard_to = StandardScaler()

def predict(Year, Current_Price, Dist_Driven, Owner, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual):
    Fuel_Type_Diesel = 0
    if (Fuel_Type_Petrol == 'Petrol'):
        Fuel_Type_Petrol = 1
    else:
        Fuel_Type_Diesel = 1
        Fuel_Type_Petrol = 0
    Year = 2020 - Year
    if (Seller_Type_Individual == 'Individual'):
        Seller_Type_Individual = 1
    else:
        Seller_Type_Individual = 0
    if (Transmission_Mannual == 'Mannual'):
        Transmission_Mannual = 1
    else:
        Transmission_Mannual = 0

    # Prediction
    prediction = model.predict([[Current_Price, np.log(Dist_Driven), Owner, Year, Fuel_Type_Diesel, Fuel_Type_Petrol,
                                 Seller_Type_Individual, Transmission_Mannual]])
    output = round(prediction[0], 2)

    # Output
    if (output < 0):
        return "Sorry, You cannot sell this car"
    else:
        return "The current value of the car is {} lakhs.".format(output)

def main():
    st.title("Car Price Prediction App")
    Year = st.number_input("Year of Purchase", min_value=1950, max_value=2022, step=1)
    Current_Price = st.number_input("Current Price (in lakhs)", min_value=0.0, max_value=100.0, step=0.1)
    Dist_Driven = st.number_input("Distance Driven (in kilometers)", min_value=0, max_value=1000000, step=1000)
    Owner = st.number_input("Number of Owners", min_value=0, max_value=10, step=1)
    Fuel_Type_Petrol = st.selectbox("Fuel Type", ("Petrol", "Diesel"))
    Seller_Type_Individual = st.selectbox("Seller Type", ("Individual", "Dealer"))
    Transmission_Mannual = st.selectbox("Transmission", ("Mannual", "Automatic"))

    if st.button("Predict"):
        result = predict(Year, Current_Price, Dist_Driven, Owner, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual)
        st.write(result)

if __name__ == "__main__":
    main()
