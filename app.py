import numpy as np
import streamlit as st
import pandas as pd
import tensorflow as tf

age = pd.read_csv('age_codes.csv')
gender = pd.read_csv('gender_codes.csv')
merchant = pd.read_csv('merchant_codes.csv')
category = pd.read_csv('category_codes.csv')

model = tf.keras.models.load_model('Ann.h5')

st.title('Transaction Fraud Detection')
age_cat = st.selectbox('Age Category', age.columns)
gender_cat = st.selectbox('Gender', gender.columns)
merchant_cat = st.selectbox('Merchant', merchant.columns)
cat = st.selectbox('Category of Expense', category.columns)
amount = st.number_input('Expense $')

if st.button('Submit'):
    array = [age[age_cat][0], gender[gender_cat][0], merchant[merchant_cat][0], category[cat][0], amount]
    prediction = model.predict(np.asarray([array]))
    if prediction < 0.5:
        st.title('Valid Transaction')
        st.write('The Probability of this transaction to be VALID is :', str(np.round(1 - prediction[0][0]) * 100), '%')
    else:
        st.title('Fraud Transaction')
        st.write('The Probability of this transaction is being FRAUD is:', str(np.round(prediction[0][0] * 100)), '%')
