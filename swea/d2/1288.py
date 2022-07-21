t = int(input())

for i in range(1, t+1):
    #Input 가져오기(첫번째 값 => 1)
    N = int(input())
    N1 = N
    #set에 계속 추가 예정
    numbers = set()
    #while 반복 -> set의 길이가 10이 될 때까지
    while len(numbers) < 10 :
    #반복할 때 나오는 숫자
    #for 반복 : 숫자를 문자로
        for n in str(N) :
    #numbers set에 추가
            numbers.add(n)
        print(n, numbers)
        N += N1
    print(f'#{t} {N}')

# 1. 반복 ? 모든 수에 체크 => while
# 2. 모든 수 체크를 어떻게 할 건데??
# - 리스트(0이 없을 때까지) - 숫자지만 인덱스로 사용 가능하다 
# or 중복제거(set) 길이가 0이 될 때까지    