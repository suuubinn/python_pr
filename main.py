name = input('이름을 입력하세오: ')
print(name)

# 문자열을 정수로 변환
try:
    age = int(input('나이를 입력하세요:'))
    print(age)
except:
    print('문제발생')
print('프로그램 종료')

# 여러개 입력
hobbys = input('취미를 ,로 구분해서 입력하세요').split(',')
for hobby in hobbys:
    print(hobby)
