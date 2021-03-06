# 正则表达式匹配


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(p), len(s)
        # dp[i][j]表示p串的前i个字符能否与s串的前j个字符匹配
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, m + 1):
            if p[i - 1] == '*':
                dp[i][0] = dp[i - 2][0]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[i - 1] == '*':
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        dp[i][j] = dp[i][j - 1] or dp[i - 2][j]
                    else:
                        dp[i][j] = dp[i - 2][j]
                else:
                    if p[i - 1] == s[j - 1] or p[i - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]
