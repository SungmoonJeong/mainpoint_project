import streamlit as st
import folium
from streamlit_folium import folium_static
import json
from exchange_rate import run_exchange_rate_app  # 환율 데이터 가져오기 함수

def add_popup(feature, country_name, exchange_rate):
    popup_html = f"<b>{country_name}</b><br>"
    popup_html += f"환율: {exchange_rate}"
    return popup_html

@st.cache_resource
def map_create_with_exchange_rate():
    # 환율 데이터 가져오기
    df_exchange_rate = run_exchange_rate_app()

    Europe = ['그리스', '네덜란드', '독일', '룩셈부르크', '몰타', '벨기에', '스페인', '슬로바키아', '아일랜드', '오스트리아', '이탈리아', '키프로스', '포르투갈', '프랑스', '핀란드']

    # 지도 생성
    m = folium.Map(location=[35.762887375145795, 84.08313219586536], zoom_start=3,
                   max_bounds=True,
                   min_zoom=2, min_lat=-84,
                   max_lat=84, min_lon=-175, max_lon=187)

    # GeoJSON 파일 경로
    geo_data = 'World_Countries__Generalized_.geojson'

    # GeoJSON 데이터 로드
    with open(geo_data, 'r', encoding='utf-8') as f:
        jsonData = json.load(f)

    # GeoJSON 데이터를 지도에 추가
    for feature in jsonData['features']:
        country_name = feature['properties']['나라']  # GeoJSON 파일의 국가 이름 속성명으로 지정
        
        # 기본 색상은 흰색으로 설정
        fillColor = 'white'
        
        # 국가 이름으로 환율 데이터프레임에서 찾기
        exchange_rate_row = df_exchange_rate[df_exchange_rate['cur_nm'].str.contains(country_name, na=False, case=False)]
        
        # Europe 리스트에 있는 국가이면서 '유로' 환율 데이터가 있는 경우
        if country_name in Europe:
            euro_exchange_rate = df_exchange_rate[df_exchange_rate['cur_nm'] == '유로']['deal_bas_r'].iloc[0]
            fillColor = 'blue'
            popup = add_popup(feature, country_name, euro_exchange_rate)
        elif not exchange_rate_row.empty:
            fillColor = 'red'
            popup = add_popup(feature, country_name, exchange_rate_row['deal_bas_r'].iloc[0])
        else:
            popup = add_popup(feature, country_name, '데이터 없음')
        
        # GeoJSON을 Folium의 GeoJson 객체로 추가
        folium.GeoJson(
            feature,
            name='json_data',
            style_function=lambda x, fillColor=fillColor: {
                'fillColor': fillColor,
                'color': 'black',
                'weight': 2,
                'fillOpacity': 0.5
            },
            tooltip=folium.features.GeoJsonTooltip(fields=['나라'], aliases=['Country']),
            popup=folium.Popup(popup, max_width=300)
        ).add_to(m)

    return m

def page3_display():
    st.title("페이지3")
    st.write("여기는 페이지 3입니다.")
    
    folium_map = map_create_with_exchange_rate()
    folium_static(folium_map)

# Run the display function
page3_display()
