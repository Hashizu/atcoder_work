S = input()

dp = [[0]*len(S) for i in range(len("chokudai"))]
for i, c in enumerate("chokudai"):
    for si, s in enumerate(S):
        if (c =="c") & (s=="c"):
            dp[0][si] = dp[0][si-1] + 1
        elif c == s:
            dp[i][si] = dp[i][si-1] + dp[i-1][si]
        else:
            dp[i][si] = dp[i][si-1]

print(dp[-1][-1] % (10**9+7))S = input()

dp = [[0]*len(S) for i in range(len("chokudai"))]



for i, c in enumerate("chokudai"):
    for si, s in enumerate(S):
        if (c =="c") & (s=="c"):
            dp[0][si] = dp[0][si-1] + 1
        elif c == s:
            dp[i][si] = dp[i][si-1] + dp[i-1][si]
        else:
            dp[i][si] = dp[i][si-1]

print(dp[-1][-1] % (10**9+7))