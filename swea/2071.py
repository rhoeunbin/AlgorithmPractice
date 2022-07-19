import sys

sys.stdin = open("input.txt", "r")

t=int(input())
for i in range(1,t+1) : 
    n = list(map(int, input().split()))
    avg = sum(n)/len(n)
    avg = round(avg)
    print(f'#{i} {avg}')
