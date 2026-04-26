import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts

# st.color_picker('rr')
# st.badge("New", color="primary", icon="🔥")
# st.link_button('Click', 'https://google.com/')

st.set_page_config(page_title="Auto check", layout="wide", initial_sidebar_state='expanded')
df = pd.read_excel('8d_check/scored_report.xlsx')
st.dataframe(df)

max_score = 20
option = {
    "title": {"text": "8D Report Quality Profile"},
    "legend": {
        "data": ["report 1", "report 2"]
    },
    "radar": {
        "splitNumber": 4,
        "indicator": [
            {"name": "Cause of Occurrence", "max": max_score},
            {"name": "Correction Actions of Occurrence", "max": max_score},
            {"name": "Reason of Escape out", "max": max_score},
            {"name": "Correction Actions of Escape out", "max": max_score},
            {"name": "Prevention Actions", "max": max_score},
            {"name": "Standardization", "max": max_score},
        ]
    },
    "series": [
        {
            "name": "reports",
            "type": "radar",
            "data": [
                {
                    "value": list(df['score']),
                    "name": "report 1",
                },
            ],
        }
    ],
}
st_echarts(option, height="500px")

def draw_gauge(data, key, height="300px"):
    options = {
        "series": [
            {
                "type": "gauge",
                "startAngle": 180,
                "endAngle": 0,
                "min": 0,
                "max": 20,
                "splitNumber": 4,
                "progress": {"show": False, "width": 18},
                "axisLine": {"lineStyle": {"width": 18, "color": [
                                                                    [0.25, '#E44343'], # 0-25% 顏色
                                                                    [0.5, '#E47E43'], # 25%-50% 顏色
                                                                    [0.75, '#F9E554'],    # 50%-75% 顏色
                                                                    [1, '#82D270'] #75%-100% 顏色
                                                                    ]}},
                "axisTick": {"show": False},
                "splitLine": {"length": 15, "lineStyle": {"width": 2, "color": "#999"}},
                "axisLabel": {"distance": 25, "color": "#999", "fontSize": 20},
                "anchor": {
                    "show": False,
                },
                "title": {"show": False},
                "detail": {
                    "valueAnimation": True,
                    "fontSize": 40,
                    "offsetCenter": [0, "30%"],
                },
                "pointer": {
                  "icon": 'diamond',
                  "length": '80%',
                  "width": 10,
                  "offsetCenter": [0, '0%'],
                  "itemStyle": {"color": 'auto'}
                },
                "data": [{"value": data}],
            }
        ]
    }
    st_echarts(options, height=height, key=key)

col1, col2, col3 = st.columns(3, border=True)
col4, col5, col6 = st.columns(3, border=True)
items = ['Cause of Occurrence', 'Correction Actions of Occurrence',
       'Reason of Escape out', 'Correction Actions of Escape out',
       'Prevention Actions', 'Standardization']
df_dict = df.set_index('項目').to_dict('index')
with col1:
    item = items[0]
    st.subheader(item, text_alignment='center')
    draw_gauge(data=df_dict[item]['score'], key='chart1')
    st.caption(df_dict[item]['suggestion'])
with col2:
    item = items[1]
    st.subheader(item, text_alignment='center')
    draw_gauge(data=df_dict[item]['score'], key='chart2')
    st.caption(df_dict[item]['suggestion'])
with col3:
    item = items[2]
    st.subheader(item, text_alignment='center')
    draw_gauge(data=df_dict[item]['score'], key='chart3')
    st.caption(df_dict[item]['suggestion'])
with col4:
    item = items[3]
    st.subheader(item, text_alignment='center')
    draw_gauge(data=df_dict[item]['score'], key='chart4')
    st.caption(df_dict[item]['suggestion'])
with col5:
    item = items[4]
    st.subheader(item, text_alignment='center')
    draw_gauge(data=df_dict[item]['score'], key='chart5')
    st.caption(df_dict[item]['suggestion'])
with col6:
    item = items[5]
    st.subheader(item, text_alignment='center')
    draw_gauge(data=df_dict[item]['score'], key='chart6')
    st.caption(df_dict[item]['suggestion'])