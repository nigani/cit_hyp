import plotly.graph_objects as go
import plotly.express as px

import pandas as pd
import numpy as np

import streamlit as st

st.set_page_config(
    page_title="ЦП 2021: Hyper AdTech",
    layout='wide',
    initial_sidebar_state='auto',
)

# st.markdown(
#     """
#     <style>
#     #MainMenu {visibility: hidden; }
#     footer {visibility: hidden;}</style>
#     """,
#     unsafe_allow_html=True
# )


def next_step():
    save_pages = st.session_state.pages
    next_page_id = pages[st.session_state.page]['id'] + 1
    if next_page_id > 10:
        next_page_id = 0
    st.session_state.page = list(save_pages.keys())[next_page_id]


def main_page():
    st.title("Цифровой портрет")
    st.write(
        """
        
        Решение расположено по ссылке:
        https://35f26fb0-5823-43fa-8575-6faabd4fc642.yds.yandexcloud.net/lab/b1gctc9hoqtkkl92j7qa/918b0c26-3a18-470b-b9e3-c3bfcecc2669/35f26fb0-5823-43fa-8575-6faabd4fc642/?token=fc82ad82-f4ae-4b3d-a0e1-c4c93dfac287
        
        ## • Загрузите известные данные
        ## • Загрузите информацию о сессиях
        ## • Наложите дополнительную фильтрацию при желании
        ## • Получите цифровой портрет
        ###
        
        """
    )

    st.button("ПРИСТУПИТЬ")

    with st.expander("Расширенные инструкции"):
        st.write(
            """
            Также Вы сможете:
            * Проанализировать зависимость сегментов от цифрового следа
            * Ознакомится с распределением сегментов по фильтрам
            """
        )



st.sidebar.title(f"Меню")

with st.sidebar.expander("О сервисе"):
    st.write("## ЦИФРОВОЙ ПРОРЫВ 2021 \n Команда DST-OFF")
    st.write("Решение по определению цифрового портрета аудитории в мобильной среде")
    st.caption("Сервис разработан в рамках конкурса [Цифровой прорыв 2021. Агротех]"
               "(https://leadersofdigital.ru) по заказу "
               "Hyper AdTech")

main_page()
