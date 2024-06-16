import streamlit as st
import folium
from streamlit_folium import folium_static
import json
import os
<<<<<<< HEAD

def map_create():
=======
import pandas as pd

def map_basic():
>>>>>>> 9a388cb (thrid commit)
    # 지도 생성
    map = folium.Map(location=[35.762887375145795, 84.08313219586536], zoom_start=3,
                    max_bounds=True, 
                    min_zoom=2, min_lat=-84, 
                    max_lat=84, min_lon=-175, max_lon=187)

    # GeoJSON 파일 경로
    geo_data = 'World_Countries__Generalized_.geojson'

    # 파일 경로 확인
    if not os.path.isfile(geo_data):
        raise FileNotFoundError(f"GeoJSON 파일을 찾을 수 없습니다: {geo_data}")

    # GeoJSON 데이터 로드
    with open(geo_data, 'r', encoding='utf-8') as f:
        jsonData = json.load(f)

    # GeoJSON 데이터를 지도에 추가
    folium.GeoJson(jsonData, name='json_data',
                style_function=lambda feature: {
                    'fillColor': 'blue' if feature['properties']['COUNTRY'] == 'Mexico' else 'red',
                    'color' : 'black',
                    'weight': 2,
                    'fillOpacity': 0.5
                },
                # 클릭 이벤트 처리
                highlight_function=lambda x: {'weight':3, 'fillOpacity':0.7},
                # 팝업 설정
                tooltip=folium.features.GeoJsonTooltip(fields=['COUNTRY'], aliases=['Country']),
                popup=folium.features.GeoJsonPopup(fields=['COUNTRY'], aliases=['Country'], parse_html=True)
                ).add_to(map)

    return map

<<<<<<< HEAD
# Streamlit 앱에 지도 표시
st.title("World Map with Country Popups")
folium_static(map_create())
=======

# 지도 만들기
def map_create():
    # 지도 위험성 관련 데이터프레임 가져오기
    df = pd.read_csv("risk.csv")

    # GeoJSON 파일 경로
    geo_data = 'World_Countries__Generalized_.geojson'

    # 파일 경로 확인
    if not os.path.isfile(geo_data):
        raise FileNotFoundError(f"GeoJSON 파일을 찾을 수 없습니다: {geo_data}")

    # GeoJSON 데이터 로드
    with open(geo_data, 'r', encoding='utf-8') as f:
        jsonData = json.load(f)

    # GeoJSON features를 반복하면서 스타일 적용
    for idx, feature in enumerate(jsonData['features']):
        country_name = feature['properties']['나라']  # 국가 이름 가져오기
        # 국가 이름으로 위험도 확인
        if country_name in df['국가'].values:
            risk_level = df.loc[df['국가'] == country_name, '위험도'].values[0]
            # 위험도에 따라 fillColor 설정
            if risk_level == 1.0:
                fill_color = 'blue'
            elif risk_level == 2.0:
                fill_color = 'yellow'
            elif risk_level == 3.0:
                fill_color = 'red'
            elif risk_level == 4.0:
                fill_color = 'black'
            else:
                fill_color = 'grey'  # 기타 색상

            # 스타일을 properties에 추가
            jsonData['features'][idx]['properties']['style'] = {
                'fillColor': fill_color,
                'color': 'black',
                'weight': 2,
                'fillOpacity': 0.5
            }
        else:
            # df에 해당 국가가 없는 경우 기본 회색 스타일 적용
            jsonData['features'][idx]['properties']['style'] = {
                'fillColor': 'white',
                'color': 'black',
                'weight': 2,
                'fillOpacity': 0.5
            }

    # folium 지도 생성
    map = folium.Map(location=[35.762887375145795, 84.08313219586536], zoom_start=3,
                     max_bounds=True, 
                     min_zoom=2, min_lat=-84, 
                     max_lat=84, min_lon=-175, max_lon=187)

    # GeoJSON 데이터를 지도에 추가
    folium.GeoJson(
        jsonData,
        name='json_data',
        style_function=lambda feature: {
            'fillColor': feature['properties']['style']['fillColor'],
            'color': feature['properties']['style']['color'],
            'weight': feature['properties']['style']['weight'],
            'fillOpacity': feature['properties']['style']['fillOpacity']
        },
        highlight_function=lambda x: {'weight': 3, 'fillOpacity': 0.7},
        tooltip=folium.features.GeoJsonTooltip(fields=['COUNTRY'], aliases=['Country']),
        popup=folium.features.GeoJsonPopup(fields=['COUNTRY'], aliases=['Country'], parse_html=True)
    ).add_to(map)

    return map

 
>>>>>>> 9a388cb (thrid commit)
