alp = list(input())  #알파벳을 리스트에 넣어줌

for i in range(len(alp)) :
    result = (ord(alp[i])-64)  #대문자 A가 65이기 때문에 64를 빼면 1부터 출력
    print(result,end=' ')