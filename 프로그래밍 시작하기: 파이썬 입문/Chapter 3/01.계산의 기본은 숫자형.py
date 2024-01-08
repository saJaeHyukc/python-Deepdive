# 파이썬 지원 자료형

"""
int: 정수
float: 실수
complex: 복소수
bool: 불린
str: 문자열(시퀀스)
list: 리스트(시퀀스)
tuple: 튜플(시퀀스)
set: 집합
dict: 사전
"""

# 데이터 타입 
str1 = "Python"
bool = True
str2 = 'Anaconda'
float = 10.0 # 10 == 10.0 False
int = 7
list = [str1, str2]
dict = {
    "name": "Machine Learning",
    "version": 2.0
}
tuple = (7, 8, 9)  # 7, 8, 9 도 가능
set = {3, 5, 7}

# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float))
print(type(int))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))

# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) : x의 y 제곱 = x ** y 
"""

# 정수 선언
i = 77
i2 = -14
big_int = 777778888777777777777777777777777

# 정수 출력
print(i)
print(i2)
print(big_int)

# 실수 선언
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

# 실수 출력
print(f)
print(f2)
print(f3)
print(f4)

# 연산 실습
i1 = 39
i2 = 939
big_int1 = 77777777777777777777777712371273727137
big_int2 = 1231231812321838123921481238421382183812
f1 = 1.234
f2 = 3.939

# +
print(">>>>> + ")
print("i1 + i2 : ", i1 + i2) 
print("f1 + f2 : ", f1 + f2) 
print("big_int1 + big_int2 : ", big_int1 + big_int2) 

# *
print(">>>>> * ")
print("i1 * i2 : ", i1 * i2)
print("f1 * f2 : ", f1 * f2)
print("big_int1 * big_int2 : ", big_int1 * big_int2)

a = 3 + 1.0
print(a) # 4.0
print(type(a)) # <class 'float'>
# Tip) 서로 다른 형을 계산을 하면 형 변환이 자동으로 이루어진다.
