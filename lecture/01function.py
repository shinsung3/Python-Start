"""
01. function
"""

def function():
    print("Hello World")

print("HI")
function()

def sum(a,b):
    sum = a+b
    print(sum)

sum(3,4)

def addTen(a):
    if a > 10:
        a = a + 5
    else:
        a = a + 10
    return a

b = addTen(11)
print(b)

def calculate (a,b,c):
    #1. 더한 값
    sum = a+b
    #2. 곱하기
    mul = a*b
    #3. 나누기
    div = a/b
    #4. 나머지값
    rem = a%b
    #5. 제곱
    pow = a**b
    #6. c
    return sum, mul, div, rem, pow, c

print(calculate(10,4,9))
a,b,c,d,e,f,g = calculate(10,4,9)
print(a,b,c,d,e,f)

## 개발자 - 변수명 선언
# session을 가져와서 넣겠다.getSessionData get_session_data
a = getSessionData # camel case
b = get_session_data #snake case
c = get-session-data #
d = GET_SESSION_DATA
e = getSessDat #fullName -> 줄여쓰지 x
