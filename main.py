import streamlit as st
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
        col1, col2, col3 = st.columns([3, 2, 2])
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
        col1, col2, col3 = st.columns([3,2,2])
        with col1:
            page3.page3_display()
        with col2:
            df =  run_exchange_rate_app()
            st.dataframe(df)
        with col3:
            page3.page3_barchart()

if __name__ == '__main__':
    main()
