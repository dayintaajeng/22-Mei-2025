import streamlit as st
import panda as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accurary_score

st.set_page_config(page_tittle="Dashbord")
st.title("Dashbord")
st.sidebar.header("Dashbord")
