import streamlit as st
import pandas as pd
from joblib import load
from sklearn.metrics import accuracy_score

model = load('car_price_model.joblib')


st.set_page_config(page_title=' app',layout='centered')
st.title('bu app emas')
st.markdown('bu markdown!')
