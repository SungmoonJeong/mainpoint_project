# sidebar.py

import streamlit as st

def sidebar_menu():
    menu = ['Home', 'EDA', 'ML', 'About', 'Exchange_rate']
    choice = st.sidebar.selectbox('메뉴', menu)
    return choice

def option_menu(label, options, icons=None, menu_icon=None, default_index=0, styles=None):
    styles = styles or {}
    container_style = styles.get("container", "")
    icon_style = styles.get("icon", "")
    nav_link_style = styles.get("nav-link", "")
    nav_link_selected_style = styles.get("nav-link-selected", "")

    with st.sidebar:
        if menu_icon:
            st.markdown(f'<i class="{menu_icon}"></i>', unsafe_allow_html=True)
        for i, option in enumerate(options):
            selected = (i == default_index)
            icon = icons[i] if icons else ""
            icon_html = f'<i class="{icon}" style="{icon_style}"></i>' if icon else ""
            link_style = nav_link_selected_style if selected else nav_link_style
            st.markdown(f'{icon_html}<span style="{link_style}">{option}</span>', unsafe_allow_html=True)

    