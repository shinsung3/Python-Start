"""
02. 문자열
.format
"""

name = "홍길동"
age = 20
marriage = False
gender ="남"
height = 170.8

#이름:  홍길동 나이 : 20 결혼여부 : False 성별:  녀 키:  170

base = "이름 : {}, 나이: {}, 결혼여부: {}, 성별: {}, 키: {}"
answer = base.format(name, age, marriage, gender, height)
print(answer)

## 가위 바위 보
mine = "가위"
yours = "바위"
result = "lose"
print("나는 {}, 너는 {}, 결과: {}".format(mine,yours, result))
print("""          Seoul     10,312,545        +91,375
          Pusan      3,567,910         +5,868
        Incheon      2,758,296        +64,888
          Daegu      2,511,676        +17,230
        Gwangju      1,454,636        +29,774""")