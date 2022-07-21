#시계
t = int(input())

for i in range (1, t+1) :
    h, m, a, b = map(int, input(). split())   #들어갈 4개의 숫자를 map 함수를 사용
    
    h_time = h + a
    m_time = m + b

#if ~ if문의 경우 항상 두 if문의 조건을 모두 체크
#if ~ elif 문의 경우 앞의 if문이 만족되면 뒤의 elif 문 조건은 체크 X

    if h_time > 12 : 
        h_time -= 12
    if m_time > 60 :
        m_time -= 60 
        h_time += 1
        
    print("#{} {} {}". format(i, h_time, m_time))