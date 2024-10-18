# 至此，带备忘录的递归解法的效率已经和迭代的动态规划解法一样了。
# 实际上，这种解法和迭代的动态规划已经差不多了，只不过这种方法叫做「自顶向下」，动态规划叫做「自底向上」。
# 啥叫「自顶向下」？从一个规模较大的原问题比如说 f(20)，向下逐渐分解规模，直到 f(1) 和 f(2) 这两个 base case，然后逐层返回答案
from collections import deque


# 啥叫「自底向上」？反过来，我们直接从最底下，最简单，问题规模最小的 f(1) 和 f(2) 开始往上推，直到推到我们想要的答案 f(20)，
# 这就是动态规划的思路，这也是为什么动态规划一般都脱离了递归，而是由循环迭代完成计算。

# 不同面额硬币，凑n元最少多少张
def coinChange(coins, amount: int):
    # 备忘录
    memo = dict()

    def dp(n):
        # 查备忘录，避免重复计算
        if n in memo:
            return memo[n]
        # base case
        if n == 0:
            return 0
        if n < 0:
            return -1
        res = float('INF')
        for coin in coins:
            subproblem = dp(n - coin)
            if subproblem == -1:
                continue
            res = min(res, 1 + subproblem)

        # 记入备忘录
        memo[n] = res if res != float('INF') else -1
        return memo[n]

    return dp(amount)


def coinChange2(coins, amount: int) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin < 0:
                continue
            else:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[-1] if dp[-1] != amount + 1 else -1


# 下面两题实际上是自底而上寻找递推
# f(i)表示以index为i的数结尾的连续子数组最大和，即求max{f(i)}.
# 递推为 f(i+1) = max{num[i],f(i)+nums[i+1]}.
def maxSubArray(nums):
    pre = nums[0]
    maximum = nums[0]
    for i in range(1, len(nums)):
        pre = max(nums[i], pre + nums[i])
        maximum = max(maximum, pre)
    return maximum


def maxProduct(nums) -> int:
    curmax = nums[0]
    curmin = nums[0]
    ans = nums[0]
    for i in range(1, len(nums)):
        temp = curmin
        curmin = min(curmin * nums[i], nums[i], curmax * nums[i])
        curmax = max(temp * nums[i], nums[i], curmax * nums[i])
        ans = max(curmin, curmax, ans)
    return ans


# lc 1696 given an array, jump from the first to the last one, can jump at most k numbers a time.
# minimum of sum of numbers visited
def maxResult(nums, k):
    n = len(nums)
    deq = deque()
    deq.append(0)
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = nums[i] + dp[deq[0]]  # Maximum Value in deque within that window
        if deq[0] < i - k + 1:
            deq.popleft()  # Check whether left bound is still accessible or not
        while deq and dp[deq[-1]] < dp[i]:
            deq.pop()  # Update deque with current i'th element
        deq.append(i)
    return dp[-1]  # Return total score


# 至多交易三次，最大盈利
def maxProfit(price, k):
    # Table to store results of sub problems
    # profit[t][i] stores maximum profit
    # using at most t transactions up to
    # day i (including day i)
    n = len(price)
    profit = [[0 for _ in range(n)]
              for _ in range(k + 1)]

    # Fill the table in bottom-up fashion
    for i in range(1, k + 1):
        prevDiff = float('-inf')
        for j in range(1, n):
            prevDiff = max(prevDiff, profit[i - 1][j - 1] - price[j - 1])
            profit[i][j] = max(profit[i][j - 1], price[j] + prevDiff)
    return profit
    # profit[t][i] = max(profit[t][i-1], max{(price[i] – price[j] + profit[t-1][j]) for all j in range [0, i-1]})
    # If we carefully notice,
    # max(price[i] – price[j] + profit[t-1][j]) for all j in range [0, i-1]
    # can be rewritten as = price[i] + max(profit[t-1][j] – price[j]) for all j in range [0, i-1]
    # = price[i] + max(prevDiff, profit[t-1][i-1] – price[i-1])
    # where prevDiff is max(profit[t-1][j] – price[j]) for all j in range [0, i-2]


def longestCommonConsecutiveSubstring(a, b):
    n = len(a)
    dp = [[[0, False] for _ in range(n + 1)] for _ in range(n + 1)]
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            if b[row - 1] == a[col - 1]:
                dp[row][col][1] = True
                if dp[row - 1][col - 1][1]:
                    dp[row][col][0] = dp[row - 1][col - 1][0] + 1
                else:
                    dp[row][col][0] = 1
            else:
                dp[row][col][0] = max(dp[row - 1][col][0], dp[row][col - 1][0])
    l = dp[-1][-1][0]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dp[i][j][0] == l and dp[i][j][1]:
                return b[i - l:i]


# 0-1 背包问题
# 给你一个可装载重量为 W 的背包和 N 个物品，
# 每个物品有重量和价值两个属性。其中第 i 个物品的重量为 wt[i]，价值为 val[i]，
# 背包最多能装的价值是多少
############################
# dp[i][w] 对于前 i 个物品，当前背包的容量为 w，这种情况下可以装的最大价值是 dp[i][w]。
from typing import List


def bagValue(N: int, W: int, weight: List, val: List):
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for num in range(1, N + 1):
        for wt in range(1, W + 1):
            if weight[num - 1] < wt:
                # 装入背包并且把其他东西拿出来 或者 不装入背包
                dp[num][wt] = max(dp[num - 1][wt], dp[num - 1][wt - weight[num - 1]] + val[num - 1])
            else:
                dp[num][wt] = dp[num - 1][wt]
    return dp[-1][-1]


print(bagValue(3, 4, [2, 1, 3], [4, 2, 3]))


# (m,n)棋盘，从左上角到右下角，只能向右或者向下走，不能同一个方向上连走maxMove步，有多少种走法

def ways(m, n, maxMove):
    dp = [[[] for _ in range(n + 1)] for _ in range(m + 1)]
    for k in range(2, 4):
        if k < n + 1:
            dp[1][k].append((k, 1, 0))
        if k < m + 1:
            dp[k][1].append((1, k, 1))
    for i in range(2, m + 1):
        for j in range(2, n + 1):
            if dp[i - 1][j]:
                for item in dp[i - 1][j]:
                    if item[-1] == 0:
                        dp[i][j].append((1, 2, 1))
                    else:
                        if item[1] < maxMove - 1:
                            dp[i][j].append((1, item[1] + 1, 1))
            if dp[i][j - 1]:
                for item in dp[i][j - 1]:
                    if item[-1] == 1:
                        dp[i][j].append((2, 1, 0))
                    else:
                        if item[0] < maxMove - 1:
                            dp[i][j].append((item[0] + 1, 1, 0))
    return len(dp[-1][-1])