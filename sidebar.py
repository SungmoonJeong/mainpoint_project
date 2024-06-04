# sidebar.py

import streamlit as st

def sidebar_menu():
    menu = ['Home', 'EDA', 'ML', 'About']
    choice = st.sidebar.selectbox('메뉴', menu)
    return choice

def option_menu(label, options, icons=None, menu_icon=None, default_index=0, styles=None):
    container_style = styles.get("container") if styles else None
    icon_style = styles.get("icon") if styles else None
    nav_link_style = styles.get("nav-link") if styles else None
    nav_link_selected_style = styles.get("nav-link-selected") if styles else None

    with st.sidebar:
        if menu_icon:
            st.markdown(f'<i class="{menu_icon}"></i>', unsafe_allow_html=True)
        for i, option in enumerate(options):
            if i == default_index:
                selected = True
            else:
                selected = False

            if icons:
                icon = icons[i]
                st.markdown(f'<i class="{icon}" style="{icon_style}"></i>', unsafe_allow_html=True)
            st.markdown(f'<span style="{nav_link_selected_style if selected else nav_link_style}">{option}</span>', unsafe_allow_html=True)
