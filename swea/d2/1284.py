T = int(input())
 
for i in range(T):
    p,q,r,s,w = map(int, input().split())
    a = p * w 
    if w > r : 
        b = (w - r) * s + q
    else :
        b = q
    if a > b:
        result = b
         
    else :
        result = a
    print("#{} {}".format(i+1, result))