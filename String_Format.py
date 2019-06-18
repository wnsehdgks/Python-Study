# 문자열을 나타내는 방법 4가지
a = "Hello World"
b = 'Python is fun'
c = """Life is too short, You need Python"""
d = '''Life is too short, You need Python'''

# 문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때
food = "Python's favorite food is perl"
say = '"Python is very easy." he says.'

food = 'Pytons\'s favorite food is perl'
say = "\"Python is very easy.\" he says."

# 여러 줄인 문자열을 변수에 대입하고 싶을 때
multiline = "Life is too short\nYou need Python"

multiline = '''
Life is too short
You need Python
'''

multiline = """
Life is too short
You need Python
"""

# 그 외 이스케이프 문자
# \n	개행 (줄바꿈)
# \t	수평 탭
# \\	문자 "\"
# \'	단일 인용부호(')
# \"	이중 인용부호(")
# \r	캐리지 리턴
# \f	폼 피드
# \a	벨 소리
# \b	백 스페이스
# \000	널문자

# 문자열 더해서 연결하기
head = "Python"
tail = " is fun!"
# head+tail

# 문자열 곱하기 응용
print("="*50)
print("My Program")
print("="*50)

# 문자열 길이 구하기
a = "Life is too short"
# len(a)

# 문자열 인덱싱
a = "Life is too short, You need Python"
# a[0] a[1] a[2] ...
# a[-1] a[-2] a[-3] ...

# 문자열 슬라이싱
# a[0:4] a[19:] a[:20] a[:] a[19:-7]


print(a[0:4])
