import streamlit as st
import pandas as pd
import os

csv_PATH= os.path.join(os.path.dirname(__file__), "..", "common", "raw_trade_data.csv")
#csv_PATH= os.path.join(os.path.dirname(__file__), "raw_trade_data.csv")

#환율샘플 데이터
#딕셔너리 표만들기
exchange_data= {
    "통화": ["USD", "EUR", "JPY", "CNY"],
    "환율": ["1390", "1605", "860", "191"],
    "전일대비": ["+5.2", "-3.1", "+1.0", "-0.4"],
}


df_exchange= pd.DataFrame(exchange_data)


st.title("💱오늘의 환율 대시보드")
st.caption("아래 데이터는 실제 환율이 아닌 실습용 샘플 데이터입니다.")

st.header ("1)환율 표 보기")
st.write("st.dataframe (상호작용 가능한 표)")
st.dataframe(df_exchange, use_container_width=True)

st.write("st.datatable")
st.table(df_exchange)

st.header ("3)보너스: 무역 원본 데이터 미리 보기")
st.write("공용데이터 파일 raw_trade_data.csv를 읽어온 상위 5행입니다.")

df_trade_raw= pd.read_csv(csv_PATH, encoding='utf-8')
st.dataframe(df_trade_raw.head(5),use_container_width=True)

st.markdown("---")

#st.title("주요 환율 카드")

st.subheader("2) 주요 환율 카드 (st.metrics)")

#st.metric(라벨, 현재값,중간값)
col1,col2,col3= st.columns(3)

with col1:
    st.metric(label="USD/KRW", value="1450", delta="+5.2")
    

with col2:
    st.metric(label="EUR/KRW", value="1605", delta="-3.1")

with col3:
    st.metric(label="JYP/KRW", value="860", delta="+1.0")
