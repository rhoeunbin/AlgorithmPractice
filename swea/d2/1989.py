t = int(input())

for i in range(1, t+1) :  #입력한 t번 반복
    word = str(input())   #단어 입력
    if word == word[::-1] :   #앞으로 읽을 때랑 뒤로 읽을 때 같으면
        print("#{} {}".format(i,1))   #앞 뒤 같으면 #번호 1 출력
    else :
        print("#{} {}".format(i,0))   #다르면 #번호 0 출력
# input값
# 3
# level     
# samsung
# eye     