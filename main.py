import streamlit as st
import subtitle
import data
from home_file import run_home_app
from eda_file import run_eda_app
from ml_file import run_ml_app
from sidebar import sidebar_menu, option_menu
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import streamlit as st
import map
import folium
from streamlit_folium import folium_static
import json
import os
import map2
import requests
import pandas as pd
import datetime as dt
from exchange_rate import run_exchange_rate_app
try:
    import yaml
except ModuleNotFoundError as e:
    print("yaml 모듈이 설치되어 있지 않습니다. 필요한 경우 'pip install pyyaml'을 사용하여 설치하세요.")
    # 예외 처리 코드 추가


if __name__ == '__main__':
    
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=stauth.SafeLoader)

        ## yaml 파일 데이터로 객체 생성
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

    ## 로그인 위젯 렌더링
    ## log(in/out)(로그인 위젯 문구, 버튼 위치)
    ## 버튼 위치 = "main" or "sidebar"
    
    name, authentication_status, username = authenticator.login('main')

    # authentication_status : 인증 상태 (실패=>False, 값없음=>None, 성공=>True)
    if authentication_status == False:
        st.error("Username/password is incorrect")

    if authentication_status == None:
        st.warning("Please enter your username and password")

    if authentication_status:
        authenticator.logout("Logout","sidebar")
        st.sidebar.title(f"Welcome {name}")
    
    ## 로그인 후 기능들 작성 ##

    ###### 여기도 좀 더 자잘하게 할 게 아니라 하나만 실행해도 될 수 있게 정리 필요할수도?
    
    # Folium 맵을 Streamlit 애플리케이션에 표시
    folium_map = map2.map_create()
    folium_static(folium_map)



    # 나머지 코드는 그대로 유지
    subtitle.message()
    data.dataset()

    choice = sidebar_menu()

    if choice == 'Home':
        run_home_app()
    elif choice == 'EDA':
        run_eda_app()
    elif choice == 'ML':
        run_ml_app()
    elif choice == 'Exchange_rate':
        run_exchange_rate_app()  # 이 부분에서 run_exchange_rate_app() 함수를 호출합니다.
    elif choice == 'About':
        pass
    
    with st.sidebar:
        choice = option_menu("Menu", ["페이지1", "페이지2", "페이지3"],
                             icons=['house', 'kanban', 'bi bi-robot'],
                             menu_icon="app-indicator", default_index=0,
                             styles={
            "container": {"padding": "4!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
            "nav-link-selected": {"background-color": "#08c7b4"},
        })

    
