import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="소득 수준 및 세금 계산기", page_icon="💰", layout="centered")

st.title("💰 소득 수준 분류 및 세금 계산기")
st.write("입력한 **소득(income)** 금액에 따라 소득 수준을 분류하고 세금을 계산합니다.")

# 소득 입력
income = st.number_input("당신의 소득을 입력하세요 (원)", min_value=0, step=10000, format="%d")

# 계산 버튼
if st.button("계산하기"):
    tax = 0  # 초기값

    # if-elif-else 문을 이용해 소득 수준 분류
    if income >= 10000000:
        level = "고소득자"
        tax = income * 0.3
    elif income >= 5000000:
        level = "중간소득자"
        tax = income * 0.2
    else:
        level = "저소득자"
        tax = income * 0.1

    # 결과 출력
    st.success(f"소득 수준: **{level}**")
    st.info(f"예상 세금: **{int(tax):,}원**")

else:
    st.warning("👆 위에 소득을 입력하고 **[계산하기]** 버튼을 눌러주세요.")
