import streamlit as st
import pandas as pd
import numpy as np

from prediction import predict

st.title('Attacked or Not')
st.markdown('Machine learning model to predict attack happend or not')

st.header('Data Features')
col1, col2 = st.columns(2)
with col1:
    st.text('Message Characteristics')
    dur = st.slider('Duration (s)', 0.0, 6.0, 0.05)
    spkts = st.slider('spkts (count)', 0.0, 11000.0, 200.0)
    dpkts = st.slider('dpkts (count)', 0.0, 11018.0, 200.0)
    sbytes = st.slider('sbytes (bytes)', 0.0, 14355770.0, 5000.0)
with col2:
    st.text('Message characteristics')
    rate = st.slider('rate (s)', 0.0, 1000000.0, 10000.0)
    sttl = st.slider('sttl (s)', 0.0, 255.0, 10.0)
    dttl = st.slider('dttl (s)', 0.0, 254.0, 10.0)
    sload = st.slider('sload (s)', 0.0, 598800000.0, 100000000.0)

st.text('')
if st.button('Predict type of attack'):
    result = predict(
        np.array([[dur],[spkts],[dpkts],[sbytes],[rate],[sttl],[dttl],[sload]]))
    st.text(result[0])


st.text('')