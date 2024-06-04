import streamlit as st
import pandas as pd

def dataset():
    st.title('아이리스 꽃 데이터')

    df=pd.read_csv('iris.csv')
        
    status =st.radio('정렬을 선택하세요',['오름차순정렬','내림차순정렬'])

    
    if status == '오름차순정렬' :
        # df의 petal_length 컬럼을 오름차순으로 정렬해서 보여주세요.
        st.dataframe(df.sort_values('petal_length'))
           
    elif status == '내림차순정렬':
        # df의 petal_length 컬럼을 내림차순으로 정렬해서 보여주세요.
        st.dataframe(df.sort_values('petal_length',ascending=False))
        
