# 소득(income)과 세금(tax) 변수를 선언
income = int(input("당신의 소득을 입력하세요 (원): "))
tax = 0  # 초기값

# if-else 문을 이용해 소득 수준 분류
if income >= 10000000:
    level = "고소득자"
    tax = income * 0.3   # 세율 30%
elif income >= 5000000:
    level = "중간소득자"
    tax = income * 0.2   # 세율 20%
else:
    level = "저소득자"
    tax = income * 0.1   # 세율 10%

# 결과 출력
print("소득 수준:", level)
print("세금:", int(tax), "원")
