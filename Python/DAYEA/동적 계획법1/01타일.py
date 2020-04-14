N = int(input())
L = [1, 2]
for i in range(2,N):
    # 출력이 너무 커서 15746으로 나눈 값을 반복문 안에서도
    # 나머지 연산을 해 주어야 메모리 초과가 발생하지 않는다.
    # (값이 int값을 초과하기 때문에 n = 1000000 일 경우 엄청나게 많은 메모리를 차지하게 된다.)
    L.append((L[i-1] + L[i-2]) % 15746)
    
print(L[N-1])
