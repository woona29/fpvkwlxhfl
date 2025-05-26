import streamlit as st
st.title('나의 첫 Streamlit 앱')
st.write('안녕하세요!')
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Plotly 시각화", layout="wide")
st.title("📊 Google Drive CSV + Plotly 시각화")

# ✅ Google Drive에서 데이터 불러오기
csv_url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
df = pd.read_csv(csv_url)

# ✅ 날짜 형식 변환 (필요시)
if '날짜' in df.columns:
    df['날짜'] = pd.to_datetime(df['날짜'])

# ✅ 데이터 미리보기
st.subheader("데이터 미리보기")
st.dataframe(df.head())

# ✅ Plotly 시각화
if {'날짜', '판매량', '카테고리'}.issubset(df.columns):
    fig = px.line(df, x='날짜', y='판매량', color='카테고리', title="카테고리별 판매량 추이")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("시각화를 위해 '날짜', '판매량', '카테고리' 컬럼이 필요합니다.")
