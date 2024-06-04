import streamlit as st

def message() :

    st.success('성공했을때 메시지를 보여줄때 사용')
    st.warning('경고 메세지를 보여주고 싶을때')
    st.info('정보성 메세지를 보여주고 싶을때')
    st.error('문제가 발생했음을 보여주고 싶을때')