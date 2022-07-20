T = int(input())

for i in range(T):
    p, q, r, s, w = map(int, input().split())
    a = p * w 
    if w > r : 
        b = (w-r)*s+q
    else :
        b = q
    if a > b :
        result = b
        
    else :
        result = a
    print("#{} {}".format(i+1,result))  
    # print(f'#{i} {min(a,b)}')

    #{} {} 뒤에 값을 불러옴
    # format(값0, 값1)

