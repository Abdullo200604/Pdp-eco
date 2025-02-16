from collections import deque
import sys

input = sys.stdin.read
MAXN = 1000000
INF = MAXN + 3


def t_main():
    global n, k, l, r
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    dp = [0] * (MAXN + 5)
    dp[0] = dp[n + 1] = INF
    dp[n + 1] += 1

    for i in range(1, n + 1):
        dp[i] = int(data[i + 1])

    pos = deque()
    pos.append(k)
    isRight = (k == 1 or dp[k - 1] > dp[k])
    l = r = pos[-1]
    ans = []

    while 1 <= l or r <= n:
        if isRight:
            cur = r + 1
            r = cur
            while len(pos) > 1:
                if dp[pos[-1]] < dp[cur]:
                    ans.append(pos.pop())
                else:
                    break
            if len(pos) == 1 and dp[pos[-1]] < dp[cur]:
                isRight = not isRight
            pos.append(cur)
        else:
            cur = l - 1
            l = cur
            while len(pos) > 1:
                if dp[pos[0]] < dp[cur]:
                    ans.append(pos.popleft())
                else:
                    break
            if len(pos) == 1 and dp[pos[0]] < dp[cur]:
                isRight = not isRight
            pos.appendleft(cur)

    for i in range(n):
        print(ans[i], end=" \n"[i == n - 1])


if __name__ == "__main__":
    t = 1
    sys.stdin = open(0)
    while t > 0:
        t_main()
        print()
        t -= 1

