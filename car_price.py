import streamlit as st
import pandas as pd
from joblib import load
from sklearn.metrics import accuracy_score

model = load('car_price_model.joblib')


#Page, UI header
st.set_page_config(page_title='Find Audi used car price app',layout='centered')
st.title('Used Cars')
st.markdown('Please enter your audi car details and calculate price')

# User inputlari uchun
model_name = st.text_input('Model name')
year = st.number_input('Produced year')
transmission = st.text_input('Transmission', 'Auto')




#Prediction logic
if st.button('Calculate your car price'):
    input_date=pd.DataFrame([{
        'model':model_name,
        'year':year,
        'transmission':transmission
        
    }])
