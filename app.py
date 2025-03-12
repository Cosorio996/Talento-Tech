import streamlit as st
import numpy as np 
import pandas as pd 
import seaborn as sn 
import matplotlib as mp

dataframe = pd.DataFrame(
    np.random.randn(10, 20), ## creamos valores aleatorios 
    columns=('col %d' % i for i in range(20))) ## llenamos columnas 
st.dataframe(dataframe.style.highlight_max(axis=0)) ## highlight seleciona el valor maximo en cada columna 
