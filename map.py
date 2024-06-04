import streamlit as st
import folium
from streamlit_folium import folium_static
import json
import os

def map_create():
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
    geojson_layer = folium.GeoJson(jsonData, name='json_data',
                style_function=lambda feature: {
                    'fillColor': 'blue' if feature['properties']['COUNTRY'] == 'Canada' else 'red',
                    'color': 'black',
                    'weight': 2,
                    'fillOpacity': 0.5
                },
                # 클릭 이벤트 처리
                highlight_function=lambda x: {'weight':3, 'fillOpacity':0.7},
                # 팝업 설정
                ).add_to(map)

    for feature in jsonData['features']:
        country_name = feature['properties']['COUNTRY']
        popup_content = f"<b>{country_name}</b>"
        folium.Popup(popup_content, parse_html=True).add_to(geojson_layer)

    geojson_layer.add_to(map)
    
    return map

