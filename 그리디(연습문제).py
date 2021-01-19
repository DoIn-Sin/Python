# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.9.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # 1. 거스름돈 걸러주기 (그리디)

# ### 거스름돈으로 사용할 돈은 500, 100, 50, 10원이다. 손님에게 거슬러줘야할 돈을 N이라고 할 때, 최소한으로 거슬러줄 수 있는 동전의 개수를 구하시오.(단, N은 10의 배수이다.)

# +
N = 1260 # N을 1260원 이라고 가정함.
count = 0
money = [500, 100, 50, 10]

for i in money:
    count += N // i
    N %= i

print(count)
# -

# # 2. 가장 큰 수를 찾는 경우의 덧셈결과 출력하기 (그리디)

# ### 길이가 N인 정수형 배열에서 총 M번 더하여 가장 큰 수가 되는 경우를 찾으려고 한다. 이때, 배열의 한 숫자 당 중복 가능 횟수는 K이다. 예를들어 N, M, K 가 6, 7, 3이고 배열이 [1, 2, 3, 4, 5, 6]이면, 6+6+6+5+6+6+6=41이다.

# +
# N, M ,K를 공백 구분으로 입력받기
N, M, K = map(int, input('N(배열의 길이), M(총 덧셈 횟수), K(중복가능 횟수) 를 입력하세요 : (단, 공백으로 구분하여 입력)').split())
# N 크기의 배열을 공백 구분으로 입력받기
num = list(map(int, input('%d번 숫자를 입력하세요 : (단, 공백으로 구분하여 입력)'%N).split()))

count = 0
result = 0

num.sort(reverse=True)

for i in range(M):
    if count == K :
        count = 0
        result += num[1]
    else : 
        result += num[0]
        count += 1

print('가장 큰 수를 찾은 결과는 %d 입니다.'%result)
# -

# # 3. 숫자 카드 게임 (그리디)

# ### 다음의 룰을 따라 가장 큰 수가 적힌 숫자 카드를 뽑으시오.
# ### 1. 숫자 카드는 N x M의 형태이다.
# ### 2. 뽑을 카드의 행을 고른다.
# ### 3. 행에 포함된 카드 중에 가장 작은 수가 적힌 카드를 뽑는다.
# ### 4. 뽑을 수 있는 모든 경우 중에서 가장 큰 수가 적힌 카드를 뽑은 경우 승리.

# +
N, M = map(int, input('카드는 N x M 의 형태입니다. N과 M을 입력하세요 : (입력 예시 : 3,3) -> ').split(','))
max_val = 0

for i in range(N) : 
    print('%d행의 숫자 카드를 입력합니다.'%(i+1))
    arr = list(map(int, input('숫자 카드를 %d번 입력하세요 :'%M).split(',')))
    min_val = min(arr)
    max_val = max(max_val, min_val)
    
print('가장 큰 숫자가 적힌 숫자 카드는 %d 입니다.'%max_val)
# -

# # 4. 1로 만들기 (그리디)

# ### 어떠한 수 N, K를 입력받아 N에서 1을 빼고, N을 K로 나눠 최종적으로 N을 1로 만들려고 한다. 이때, N을 1로 만드는데 실행한 과정 횟수를 구하시오. (단, K로 나누는 경우는 N이 K로 나누어떨어질때만 실행한다.)

# +
N, K = map(int, input('숫자 N과 나누는 수 K를 입력하세요 : (입력예시 : 4,2) -> ').split(','))
while True :
    if K > N :
        print('K는 N보다 클 수 없습니다.')
        N, K = map(int, input('숫자 N과 나누는 수 K를 입력하세요 : (입력예시 : 4,2) -> ').split(','))
    else :
        break
        
count = 0

while True:
    if N != 1:
        if N % K == 0:
            N /= K
            count += 1
        else : 
            N -=  1
            count += 1
    else : 
        break
print('1로 만드는데 걸린 과정은 %d번 입니다.'%count)
# -


