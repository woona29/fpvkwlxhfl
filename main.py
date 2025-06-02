import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(page_title="은평구 의류수거함 지도", layout="wide")

# 제목
st.title("📦 은평구 의류 수거함 시각화 대시보드")
st.markdown("서울특별시 은평구에 설치된 의류 수거함 위치를 시각화한 지도입니다.")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("data/은평구_의류수거함.csv", encoding='cp949')
    df = df[['행정동', '설치장소', '위도', '경도']].dropna()
    return df

df = load_data()

# 행정동 필터
dong_list = sorted(df['행정동'].unique())
selected_dong = st.selectbox("🔍 행정동 선택", ["전체"] + dong_list)

# 필터 적용
if selected_dong != "전체":
    filtered_df = df[df['행정동'] == selected_dong]
else:
    filtered_df = df

# 지도 시각화
m = folium.Map(location=[filtered_df['위도'].mean(), filtered_df['경도'].mean()], zoom_start=14)
for _, row in filtered_df.iterrows():
    folium.Marker(
        location=[row['위도'], row['경도']],
        popup=row['설치장소'],
        icon=folium.Icon(color="green", icon="tshirt", prefix="fa")
    ).add_to(m)

st.subheader("🗺️ 수거함 위치 지도")
st_data = st_folium(m, width=800, height=500)

# 통계 시각화
st.subheader("📊 행정동별 수거함 개수")
dong_counts = df['행정동'].value_counts().sort_values(ascending=False)
st.bar_chart(dong_counts)
