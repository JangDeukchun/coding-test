# 직사각형 별찍기
# 문제 설명
# 이 문제에는 표준 입력으로 두개의 정수 n과 m이 주어집니다.
# 별을(*) 문자를 이용해 가로의 길이가n 세로의 길이가 m인 직사각형 형태를 출력해 보세요.and

# 제한 조건
# n과 m은 각각 1000 이하인 자연수 입니다.

# 예시
# 입력
# 5,3
# 출력
# *****
# *****
# *****

# 풀이
# 1. 변수 두개와 a,b 파이썬 map 함수를 이용한다.  map함수의 모양은 다음과 같다. 첫 번째 매개변수로는 함수가 오고, 두 번째 매개변수로는 반복 간으한 자료형(리스트,튜플 등)이 온다.
# ex) map(적용시킬 함수, 적용할 값을) -> map(값에+1을 더해주는 함수, [1,2,3,4,5]) = [2,3,4,5,6,]이 출력된다

# 2. 문자열 양끝 공백을 strip()함수로 제거해준다. (공백 왜 생기는지 모르겠음 이 함수를 왜 쓰는지도 모르겠음) 안써도 됨

# 3. 문자열 공백을 기준으로 나누어 주는 split('') 함수를 사용한다. 이유 : 변수두개를 동시 지정할때 (a,b와 같이) 코드 실행 후 input값을 적으려면 띄어서 적어야함.
# ex)5 3, 5,3= 오류발생. 이떄 공백이 발생하는데 split(' ')함수로 공백을 제거해 줘야 함.
a,b = map(int, input().split(' ')) # 변수 a,b는 정수형으로 input에 입력된 값 만큼 받는다.
answer = ('*'*a+'\n') * b # 변수 answer는 변수 a가 받은 수 만큼 *을 생헝하고 줄을 바꾼 후 괄호 안의 값을 변수 b가 받은 수 만큼 출력한다. 
print(answer)
