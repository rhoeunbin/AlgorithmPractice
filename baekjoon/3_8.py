t = int(input()) #테스트케이스

for i in range(t) : #t만큼 반복
    a, b =map(int,input().split())
    print(f'Case #{i+1}: {a} + {b} = {a+b}')
