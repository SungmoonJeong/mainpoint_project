import streamlit as st
import pandas as pd

def run_eda_app():
    st.subheader('EDA 화면입니다.')

    df = pd.read_csv('iris.csv')

    # 수치형 데이터만 선택
    numeric_df = df.select_dtypes(include=['float64', 'int64'])

    # 상관 계수 표시
    st.write("상관 계수:")
    st.dataframe(numeric_df.corr())

