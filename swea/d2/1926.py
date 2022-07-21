#369게임
n = int(input())  #들어갈 숫자 n

for i in range(1, n+1) : 
    t = 0      #값 초기화
    result = str(i)   #결과값 문자로 나타냄
    for j in result :  
        if j in '369':
            t += 1
    if t == 0:        
            print(result, end=" ")
    else : 
        print( '-'*t , end=" ")    