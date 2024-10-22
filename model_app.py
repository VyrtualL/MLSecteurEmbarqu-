import joblib
import streamlit as st
import pandas as pd

#st.write("hello streamlit")
#df = pd.read_csv('data.csv')

#st.write(df)
#st.line_chart(df['price'])

#name = st.text_input("Comment")
#if name:
#    st.write(f"hello {name}")

#st.sidebar.slider("temperature", 0.0, 10.0)
def load_model():
    return joblib.load('regression.joblib')

def predict():
    number = st.number_input("Insert the size, number of houses and if the house has a garden")
    predictions = load_model().predict(number)
    X = []
    st.write(predictions)