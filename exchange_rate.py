import streamlit as st
import datetime as dt
import requests
import json
import pandas as pd


def run_exchange_rate_app():
# 여기서부터는 새로 파일 만들어서 함수로 변환이 필수적입니다.
    
    #now = dt.datetime.now()
    #daily = now.strftime('%Y%m%d')    # 매 날짜 갱신해서 가져와 밑에 넣어줌으로써 데이터 갱신
    
    url = f"https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=3KBgM71Eun3za3GDai5a2kltMFmy2LYC&searchdate={20240607}&data=AP01"
    response = requests.get(url)

    # JSON 데이터를 가져옴
    json_data = response.json()

    # DataFrame으로 변환
    df = pd.DataFrame(json_data)

    # 데이터 확인
    df.drop("result", axis = 1, inplace=True)
    
    st.dataframe(df)