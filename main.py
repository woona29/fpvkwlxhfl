import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 설정
st.set_page_config(page_title="Plotly 시각화", layout="wide")

st.title("📊 Google Drive CSV 데이터 Plotly 시각화")

# 1. CSV 데이터 불러오기
csv_url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
df = pd.read_csv(csv_url)

# 2. 날짜 컬럼 변환 (필요 시)
if '날짜' in df.columns:
    df['날짜'] = pd.to_datetime(df['날짜'])

# 3. 데이터 미리보기
st.subheader("데이터 미리보기")
st.dataframe(df.head())

# 4. Plotly 시각화
required_cols = {'날짜', '판매량', '카테고리'}
if required_cols.issubset(df.columns):
    fig = px.line(df, x='날짜', y='판매량', color='카테고리', title="카테고리별 일자별 판매량 추이")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning(f"시각화를 위해 다음 컬럼이 필요합니다: {required_cols}")
