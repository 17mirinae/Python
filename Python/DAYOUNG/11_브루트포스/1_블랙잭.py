N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = 0

for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1,N):
            if (cards[i]+cards[j]+cards[k]) <= M and M - (cards[i]+cards[j]+cards[k]) < M - result:
                result = (cards[i]+cards[j]+cards[k])

print(result)
