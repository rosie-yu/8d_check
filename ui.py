import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts

def draw_gauge(data, key, height="100px"):
    options = {
        "series": [
            {
                "type": "gauge",
                "startAngle": 180,
                "endAngle": 0,
                "min": 0,
                "max": 20,
                "splitNumber": 4,
                "progress": {"show": False, "width": 11},
                "axisLine": {"lineStyle": {"width": 11, "color": [
                                                                    [0.25, '#E44343'], # 0-25% 顏色
                                                                    [0.5, '#E47E43'], # 25%-50% 顏色
                                                                    [0.75, '#F9E554'],    # 50%-75% 顏色
                                                                    [1, '#82D270'] #75%-100% 顏色
                                                                    ]}},
                "axisTick": {"show": False},
                "splitLine": {"show": False, "length": 15, "lineStyle": {"width": 2, "color": "#999"}},
                "axisLabel": {"show": False, "distance": 40, "color": "#999", "fontSize": 10},
                "anchor": {"show": False,},
                "detail": {
                    "valueAnimation": True,
                    "fontSize": 20,
                    "offsetCenter": [0, "30%"],
                },
                "pointer": {
                  "icon": 'diamond',
                  "length": '80%',
                  "width": 6,
                  "offsetCenter": [0, '0%'],
                  "itemStyle": {"color": '#999'}
                },
                "data": [{"value": data}],
            }
        ]
    }
    st_echarts(options, height=height, key=key)

# ---------------------------------------------------------------------------------------------------------------------------
st.set_page_config(page_title="8D Report Evaluator", layout="wide", initial_sidebar_state='expanded')
st.title('8D Report Evaluator')
with st.expander('評分準則'):
    guide = pd.read_excel('data/8d_data.xlsx', sheet_name='評核標準')
    st.dataframe(guide, hide_index=True)
st.subheader('Case 1')
st.caption('此結果為前置評分程式產出之已保存資料')
df = pd.read_excel('data/scored_report.xlsx')
st.dataframe(df.set_index('項目'))

# Radar Chart
st.subheader('Quality Profile')
c1,c2 = st.columns(2, vertical_alignment="center")
max_score = 20
radar_settings = {
    # "title": {"text": "8D Report Quality Profile"},
    # "legend": {
    #     "data": ["case 1", "case 2"]
    # },
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
                    "name": "case 1",
                    "itemStyle": {"color": 'rgba(39, 183, 236, 1)'},
                    "areaStyle": {"color": 'rgba(39, 183, 236, 0.3)'}
                },
            ],
        }
    ],
}
with c1:
    st_echarts(radar_settings)

# Gauge Chart
with c2:
    col1, col2, col3 = st.columns(3, vertical_alignment="bottom")
    col4, col5, col6 = st.columns(3, vertical_alignment="bottom")
    items = ['Cause of Occurrence', 'Correction Actions of Occurrence',
           'Reason of Escape out', 'Correction Actions of Escape out',
           'Prevention Actions', 'Standardization']
    df_dict = df.set_index('項目').to_dict('index')
    with col1:
        item = items[0]
        st.caption(item, text_alignment='center')
        draw_gauge(data=df_dict[item]['score'], key='chart1')
        # st.caption(df_dict[item]['suggestion'])
    with col2:
        item = items[1]
        st.caption(item, text_alignment='center')
        draw_gauge(data=df_dict[item]['score'], key='chart2')
        # st.caption(df_dict[item]['suggestion'])
    with col3:
        item = items[2]
        st.caption(item, text_alignment='center')
        draw_gauge(data=df_dict[item]['score'], key='chart3')
        # st.caption(df_dict[item]['suggestion'])
    with col4:
        item = items[3]
        st.caption(item, text_alignment='center')
        draw_gauge(data=df_dict[item]['score'], key='chart4')
        # st.caption(df_dict[item]['suggestion'])
    with col5:
        item = items[4]
        st.caption(item, text_alignment='center')
        draw_gauge(data=df_dict[item]['score'], key='chart5')
        # st.caption(df_dict[item]['suggestion'])
    with col6:
        item = items[5]
        st.caption(item, text_alignment='center')
        draw_gauge(data=df_dict[item]['score'], key='chart6')
        # st.caption(df_dict[item]['suggestion'])
    # 顏色說明
    st.markdown(":red-badge[:material/close: 差劣] :orange-badge[:material/priority_high: 普通] :yellow-badge[:material/thumb_up: 不錯] :green-badge[:material/thumbs_up_double: 傑出]",
               text_alignment="center")