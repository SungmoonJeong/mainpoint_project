import streamlit as st
<<<<<<< HEAD
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

    
=======
st.set_page_config(
    page_title = 'travel dashboard',
    page_icon="🧊",
    initial_sidebar_state="expanded",
    layout="wide",
    menu_items = {'Get Help': "https://www.extremelycoolapp.com/help",
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!" 
        }
    )

from streamlit_option_menu import option_menu
from streamlit_folium import folium_static
import map2  # map2 모듈로 임포트
from home_file import run_home_app
from eda_file import run_eda_app
from ml_file import run_ml_app
from exchange_rate import run_exchange_rate_app  # 필요한 함수 import
import data
from map2 import map_basic
import page3



def main():
    st.sidebar.title("Menu")
    with st.sidebar:  # st.sidebar에서 with 문 사용
        # 사이드바에서 메뉴 선택
        choice = option_menu("Menu", ["Home", "EDA", "ML", "Exchange_rate", "About", 'page3'],
                             icons=['house', 'bar-chart-line', 'gear-wide-connected', 'fa fa-dollar-sign', 'book'],
                             menu_icon="📱", default_index=0,
                             styles={
                                 "container": {"padding": "4!important", "background-color": "#fafafa"},
                                 "icon": {"color": "black", "font-size": "25px"},
                                 "nav-link": {"font-size": "16px", "text-align": "left", "margin": "10px 0",
                                              "--hover-color": "#fafafa"},
                                 "nav-link-selected": {"background-color": "#08c7b4"},
                             })

    # 선택된 메뉴에 따라 다른 기능 실행
    if choice == 'Home':
        st.subheader('지도')
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            folium_map = map2.map_create()
            folium_static(folium_map, 400, 300)  # Folium 지도를 Streamlit에 표시
        with col2:
            st.subheader('지도 데이터셋')
        with col3:
            st.subheader("그냥 빈칸이다.")

    elif choice == 'EDA':
        run_eda_app()
        st.subheader('데이터 탐색 및 시각화')

    elif choice == 'ML':
        run_ml_app()
        st.subheader('머신 러닝 모델 학습')

    elif choice == 'Exchange_rate':
        st.subheader('환율 데이터')
        df_exchange_rate = run_exchange_rate_app()
        st.dataframe(df_exchange_rate)

    elif choice == 'About':
        st.write("프로젝트에 대한 간단한 설명을 여기에 추가하세요.")

    elif choice == 'page3':
        page3.page3_display()

if __name__ == '__main__':
    main()
>>>>>>> 9a388cb (thrid commit)
