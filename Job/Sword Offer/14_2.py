# 剪绳子2  数据规模更大的剪绳子


class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(2, i):
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
        return dp[n] % 1000000007


if __name__ == '__main__':
    print(Solution().cuttingRope(87))
