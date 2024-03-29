# -*- coding: utf-8 -*-
"""app_compensar_aux.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17R0ff-LLRj2mhfST-yOmT0Nmnd1AGzfR
"""

import cv2
import numpy as np
from tensorflow import keras
import streamlit as st
import pandas as pd
import requests
import pickle

@st.experimental_singleton()
def load_model():
    with open("model.pkl", "rb") as f:
      model = pickle.load(f)
    return model


def predict(data):
    input_arr = np.array([data])
    y_pred = st.session_state['model'].predict(input_arr)
    y_pred = pd.DataFrame(y_pred, columns=['Si','No'])
    y_pred = y_pred * 100
    return data, y_pred