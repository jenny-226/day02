import random
from datetime import datetime

import streamlit as st


st.set_page_config(page_title="Lotto Number Generator", page_icon="L", layout="centered")
st.title("\ub85c\ub610 \ubc88\ud638 \uc790\ub3d9 \uc0dd\uc131\uae30")
st.caption("1~45 \uc0ac\uc774\uc758 \uc911\ubcf5 \uc5c6\ub294 \ubc88\ud638 6\uac1c\ub85c \ub41c \uc138\ud2b8 5\uac1c\ub97c \uc0dd\uc131\ud569\ub2c8\ub2e4.")


def lotto_one_set() -> list[int]:
    """Return six unique lottery numbers from 1 through 45."""
    return sorted(random.sample(range(1, 46), 6))

#fdf//
def get_color_ball(number: int) -> str:
    """Return a colored HTML ball for one lottery number."""
    if number < 10:
        color = "#fbc400"
    elif number < 20:
        color = "#69c8f2"
    elif number < 30:
        color = "#ff7272"
    elif number < 40:
        color = "#aaaaaa"
    else:
        color = "#b0d840"

    return (
        '<span style="display:inline-flex;align-items:center;justify-content:center;'
        f'width:36px;height:36px;margin:3px;border-radius:50%;background:{color};'
        f'color:white;font-weight:bold;">{number}</span>'
    )


st.markdown("---")

if st.button("5\uc138\ud2b8 \ubc88\ud638 \uc0dd\uc131\ud558\uae30", key="lotto_generate_btn"):
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.write(f"\uc0dd\uc131 \uc2dc\uac01: **{now_str}**")

    for set_index in range(1, 6):
        lotto_numbers = lotto_one_set()
        balls = "".join(get_color_ball(number) for number in lotto_numbers)
        st.markdown(f"**{set_index}\uc138\ud2b8** {balls}", unsafe_allow_html=True)
