def solution(n):
    count = 0

    while n != 1:
        if n % 2 != 0: #n이 2로 나누어 떨어지지 않을 경우
            count += 1
            n = n-1
        else:  #2로 나누어 떨어질 경우
            n = n/2

    return count+1

#알고리즘
#건전지 사용량이 최소가 되려면, 순간이동을 최대한 많이 해야된다.
#순간이동은 현재 위치에서 2^n만큼 이동하기 때문에
#n을 2로 나누어 떨어지지 않을 때 까지 나눈다.
#n이 2로 나누어 떨어지지 않게 되면 n-1을 해(1 점프) n을 짝수로 만든다.
#이 과정을 n이 1이 될 때 까지 반복하고 마지막에 Count +1 (1점프)를 한다.
