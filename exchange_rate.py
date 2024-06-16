import streamlit as st
import datetime as dt
import requests
import json
import pandas as pd
from map2 import map_basic, map_create
import folium
import pandas as pd
import os

def run_exchange_rate_app():
# 여기서부터는 새로 파일 만들어서 함수로 변환이 필수적입니다.    
    #now = dt.datetime.now()
    #daily = now.strftime('%Y%m%d')    # 매 날짜 갱신해서 가져와 밑에 넣어줌으로써 데이터 갱신, 작성해야
    
    url = f"https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=3KBgM71Eun3za3GDai5a2kltMFmy2LYC&searchdate={20240613}&data=AP01"
    response = requests.get(url, verify=False)

    # JSON 데이터를 가져옴
    json_data = response.json()

    # DataFrame으로 변환
    df = pd.DataFrame(json_data)

    # 데이터 확인
    df.drop("result", axis = 1, inplace=True)
    
    st.success('환율 데이터프레임')

    df['cur_nm'] = df['cur_nm'].str.replace(' 디르함', '')
    df['cur_nm'] = df['cur_nm'].str.replace(' 달러', '')
    df['cur_nm'] = df['cur_nm'].str.replace(' 디나르', '')
    df['cur_nm'] = df['cur_nm'].str.replace(' 프랑', '')
    df['cur_nm'] = df['cur_nm'].str.replace('위안화', '중국')
    df['cur_nm'] = df['cur_nm'].str.replace('덴마아크 크로네', '덴마크')
    df['cur_nm'] = df['cur_nm'].str.replace(' 파운드', '')
    df['cur_nm'] = df['cur_nm'].str.replace(' 루피아', '')
    df['cur_nm'] = df['cur_nm'].str.replace(' 엔', '')
    df['cur_nm'] = df['cur_nm'].str.replace(' 원', '')
    df['cur_nm'] = df['cur_nm'].str.replace(' 링기트', '')
    df['cur_nm'] = df['cur_nm'].str.replace(' 리알', '')
    df['cur_nm'] = df['cur_nm'].str.replace(' 링기트', '')
    df['cur_nm'] = df['cur_nm'].str.replace(' 크로나', '')
    df['cur_nm'] = df['cur_nm'].str.replace(' 바트', '')
    df['cur_nm'] = df['cur_nm'].str.replace(' 리알', '')
    df['cur_nm'] = df['cur_nm'].str.replace(' 크로네', '')
    df['cur_nm'] = df['cur_nm'].str.replace('사우디 리얄', '사우디아라비아')
    
    st.dataframe(df)
    return df

