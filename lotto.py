#로또v1

import streamlit as st
import random
from datetime import datetime

st.title(" 로또 번호 자동 생성기")
st.caption("버튼을 누르면 1~45 사이의 중복 없는 번호 6개짜리 세트를 5개 만든다")

def lotto_one_set() -> list:
 """ 1~45 에서 중복없이 번호 6개 뽑아 정렬된 리스트로 반환""" 
 number = set() # set[int]() 대신 set() 으로 수정!
 while len(number) < 6:
 number.add(random.randint(1,45)) # 1이상 45이하 정수 하나 뽑기
 return sorted(number)

def get_color_ball(num: int) -> str:
 """ 숫자에 따라 10단위로 다른 색깔 공 이모티콘을 붙여주는 함수 """
 if num < 10: # 1 ~ 9
 return f" {num}"
 elif num < 20: # 10 ~ 19
 return f" {num}"
 elif num < 30: # 20 ~ 29
 return f" {num}"
 elif num < 40: # 30 ~ 39
 return f" {num}"
 else: # 40 ~ 45
 return f" {num}"

st.markdown("---")

# if문을 써서 '버튼이 눌렸을 때'만 아래 블록이 실행되도록 만들기
if st.button(" 5세트 번호 생성하기", key="lotto_generate_btn"):
 
 # 시간 띄우기
 now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 st.write(f"생성 시각 : **{now_str}**")
 
 # 5세트 반복해서 뽑고 출력하기
 for set_index in range(1, 6):
 lotto_num = lotto_one_set() # 번호 6개 뽑기 (예: [3, 15, 22, ...])
 
 # 뽑힌 숫자 하나하나를 get_color_ball 함수에 넣어서 이모티콘으로 바꾸기
 balls = [get_color_ball(n) for n in lotto_num]
 
 # 예쁘게 가로로 나열하기
 result_text = " ".join(balls)
 st.write(f"**{set_index}세트** ｜ {result_text}")