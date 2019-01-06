import re

#아래처럼 할 경우 """이후 줄바꿈을 하였기때문에 \n, park 이런식으로 첫 번째 요소로 공백이 인식됨
#공백인식이 안되게 하려면 """ park .. 과 같은 식으로 개행을 하지말고 바로 써줘야함
data ="""
park 920804-1332453
kim 030403-1495833
"""

# \d :숫자
pat = re.compile("(\d{6})[-](\d{7})") # 문자클래스 []
print(pat.sub("\g<1>-*******",data))
#표현식을 만든다.
# data의 요소를 가져와서 해당 형식으로 replace한다.
# \g<1> = 그룹의 1번째 요소
# CH07 p32참고


print(data.split("\n"))

result = [] # 초기화
for line in data.split("\n"):
    word_result=[]
    for word in line.split(" "): #data를 공백 기준으로 split
        # print(word)
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit(): # [:6] 6자리 미만
            # word의 길이가 15자리인지 확인 / word의 [6]자리가 숫자인지 확인 / [7]번째 이후 숫자가 숫자인지 확인
            word = word[:6] + "-" + "*******"
        word_result.append(word) # word_result에 word를 append한다.

    result.append(" ".join(word_result)) # join : 문자열 연결
print("\n".join(result))




