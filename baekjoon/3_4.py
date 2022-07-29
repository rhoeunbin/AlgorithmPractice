#빠른 A+B - 시간 초과 나지 않게 풀기
import sys
t = int(input()) #테스트 케이스

for i in range(t): #t만큼의 범위동안 반복
    a, b = map(int, sys.stdin.readline().split())  
    #a,b int로 input하면 시간초과 발생
    #반복문으로 여러줄 받을 경우 sys.stidin.readline().split() 사용해 시간 줄이기
    #여러개일때 사용 개행이 들어있어서 하나의 문자에는 사용x

    print(a+b)