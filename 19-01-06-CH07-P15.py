# ctrl + 방향키 : 단어 단위로 커서이동

import re
p = re.compile('a.b')
# m = p.match('a\nb')
m = p.match('abb')
print(m)

p = re.compile('a.b', re.S) # \n을 포함하여 모든 문자와 매치한다.


import re
p = re.compile('[a-z]', re.I)
print(p.match('python')) # <re.Match object; span=(0, 1), match='p'>
print(p.match('PYTHON')) # <re.Match object; span=(0, 1), match='P'>


import re
p = re.compile("^python\s\w+")

data = """python on
life is too short
python two
you need python
python three"""

print(p.findall(data))
# ['python on']


# MULTI LINE
# 각 라인별로 메타문자를 인식시키고 싶은 경우 사용
import re
p = re.compile("^python\s\w+", re.M)

data = """python on
life is too short
python two
you need python
python three"""

print(p.findall(data))
# ['python on', 'python two', 'python three']



import re
charref = re.compile(r"""
&[#]
(
    0[0-7]+
    [0-9]+
    
)
""")


#re.compile(r'&[#](0[0-7]+[0-9]+|x[0-9a-fA-F+);')


import re
p = re.compile('Crow|Servo') #문자 두개를 찾고싶을 때 ! or연산
m = p.match('CrowHello') #이 문자열의 첫 번째 요소로 Crow or Servo가 있는지 !
print(m)
 # match : 문자열의 첫번째 요소부터 매치되어야함. 조건이 까다로워 search로 대체하여 사용
m = p.match('HelloServo')
print(m)

m=p.search('ServoHello')
print(m)


print(re.search('^Life', 'Life is too short')) # Life로 시작하는 문장 search
# <re.Match object; span=(0, 4), match='Life'> 0부터 4에 해당하는 범위 내에 있다!
print(re.search('^Life', 'My Life'))


# 현업에서는 \A, \Z보다 ^, $ 를 주로 사용

p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
# <re.Match object; span=(3, 8), match='class'>


p = re.compile(r'\sclass\s')
print(p.search('no class at all'))
# <re.Match object; span=(2, 9), match=' class '>

print(p.search('the declassfied algorithm'))
















