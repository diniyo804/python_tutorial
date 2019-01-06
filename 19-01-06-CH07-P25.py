
#문자열 중에서 이름만 뽑아내기

import re
#p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")  # r: row string
# \w : 첫번째 word
# \s : 공백
# \d : 숫자

p = re.compile(r"(\w+)\s+\d+[-](\d+)[-]\d+")
m = p.search('park 010-1234-1234')
print(m.group(0)) #문자열 전체
print(m.group(1)) #첫번째
print(m.group(2))


p = re.compile(r"(\w+)\s+((\d+)[-](\d+)[-]\d+)")
m = p.search('park 010-1234-4432')
print(m.group(3))
print(m.group(4))
# 소괄호를 이용해 그룹을 짓고 n번째 요소를 뽑아낼 수 있음
# 괄호가 중첩되어 있을 경우 범위가 큰 그룹부터 순서대로 1,2,3,4...

p = re.compile(r'(\b\w+)\s+\1')
print(p.search('Paris in the the spring').group())


