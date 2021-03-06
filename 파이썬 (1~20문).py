# 005 print 탭과 줄바꿈
# 다음 코드를 실행해보고 \t와 \n의 역할을 설명해보세요.

print("안녕하세요.\n만나서\t\t반갑습니다.")
#\t는 탭을 의미하고 \n'은 줄바꿈을 의미합니다.

# 006 print 여러 데이터 출력
print ("오늘은", "일요일")

# 007 print 기초
# print() 함수를 사용하여 다음과 같이 출력하세요.
# naver;kakao;sk;samsung
print("naver","kakado","samsung",sep=";")

# naver/kakao/sk/samsung
print("naver","kakado","samsung",sep="/")


# 009 print 줄바꿈
# 다음 코드를 수정하여 줄바꿈이 없이 출력하세요. (힌트: end='') print 함수는 두 번 사용합니다. 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.
print("first");print("second")
print("first", end="");print("second")


# 010 연산 결과 출력
print(5/3)

# 011 변수 사용하기
# 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
삼성전자 = 50000
총평가금액 = 삼성전자*10
print(총평가금액)


#012 변수 사용하기
#다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print(시가총액,type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))


#013 문자열 출력
# 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.
s = "hello"
t = "python"
# 두 변수를 이용하여 아래와 같이 출력해보세요.
# hello! python
print(s+"!",t)


#015 type 함수
# type() 함수는 데이터 타입을 판별합니다. 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.
a = 128
print (type(a))

b= "132"
print(type(b))

#문자열 '720'를 정수형으로 변환해보세요.
num_str = "720"
num_int = int(num_str)
print(num_int+1, type(num_int))


#017 정수를 문자열 100으로 변환
#정수 100을 문자열 '100'으로 변환해보세요.
num = 100
result = str(num)
print(result, type(result))


# 018 문자열을 실수로 변환
# 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
data = "15.79"
data = float(data)
print(data, type(data))


# 019 문자열을 정수로 변환
# year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
year = "2020"
print(int(year)-3)
print(int(year)-2)
print(int(year)-1)

# 020 파이썬 계산
# 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)
월 = 48584
총금액 = 월*36
print(총금액)