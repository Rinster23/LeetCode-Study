# 双指针技巧主要分为两类：左右指针和快慢指针。
# 所谓左右指针，就是两个指针相向而行或者相背而行；而所谓快慢指针，就是两个指针同向而行，一快一慢。

# 快慢指针
# leetcode 26
def removeDuplicates(nums) -> int:
    if len(nums) == 0:
        return 0
    # 维护 nums[0..slow] 无重复
    slow = 0
    fast = 1
    while fast < len(nums):
        if nums[fast] != nums[slow]:
            slow += 1
            # 维护 nums[0..slow] 无重复
            nums[slow] = nums[fast]
        fast += 1
    # 数组长度为索引 + 1
    return slow + 1


# 还有一类快慢指针就是滑动窗口问题
# left 指针在后，right 指针在前，两个指针中间的部分就是「窗口」，算法通过扩大和缩小「窗口」来解决某些问题

# 左右指针 两个指针相向或者相背而行
# 典例为在一个排好序的数组中二分查找
def binarySearch(nums, target: int) -> int:
    # 一左一右两个指针相向而行
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def longestPalindrome(s):
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

    result = ""
    for i in range(len(s)):
        sub1 = expand(i, i)  # 最长回文串长度可能是奇数也可能是偶数
        if len(sub1) > len(result):
            result = sub1
        sub2 = expand(i, i + 1)
        if len(sub2) > len(result):
            result = sub2
    return result


# 滑动窗口 左右指针确定窗口，一左一右一起向右边运动

def slidingWindow(s: str):
    # 用合适的数据结构记录窗口中的数据
    window = {}
    left = 0
    right = 0
    while right < len(s):
        # c 是将移入窗口的字符
        c = s[right]
        if c not in window:
            window[c] = 1
        else:
            window[c] += 1
        # 增大窗口
        right += 1
        # 进行窗口内数据的一系列更新
        # ...
        # 判断左侧窗口是否要收缩
        while left < right:  # and window needs shrink:
            # d 是将移出窗口的字符
            d = s[left]
            # 缩小窗口
            left += 1
            # 进行窗口内数据的一系列更新
            # ...


# leetcode 76
def minWindow(s: str, t: str) -> str:
    from collections import defaultdict

    need, window = defaultdict(int), defaultdict(int)
    for c in t:
        need[c] += 1

    left, right = 0, 0
    valid = 0
    # 记录最小覆盖子串的起始索引及长度
    start, length = 0, float('inf')
    while right < len(s):
        # c 是将移入窗口的字符
        c = s[right]
        # 扩大窗口
        right += 1
        # 进行窗口内数据的一系列更新
        if c in need:
            window[c] += 1
            if window[c] == need[c]:
                valid += 1
        # 判断左侧窗口是否要收缩
        while valid == len(need):
            # 在这里更新最小覆盖子串
            if right - left < length:
                start = left
                length = right - left  # 左闭右开

            # d 是将移出窗口的字符
            d = s[left]
            # 缩小窗口
            left += 1
            # 进行窗口内数据的一系列更新
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1

    # 返回最小覆盖子串
    return "" if length == float('inf') else s[start:start + length]


print(minWindow("ADOBECODEBANC", "ABC"))


# Given a string s, find the length of the longest substring without repeating characters
def lengthOfLongestSubstring(s: str) -> int:
    res = set()
    count = 0
    l = 0
    for r in range(len(s)):
        while s[r] in res:  # 移动左指针直到窗口中不再有重复字符
            res.remove(s[l])
            l += 1
        res.add(s[r])
        count = max(count, r - l + 1)
    return count


# 在nums中找到最多包含k个0的最长子数组
def longestOnes(nums, k: int) -> int:
    n = len(nums)
    left = lsum = rsum = 0  # lsum记录[0, left)中0的个数, rsum记录[0, right]中0的个数
    ans = 0
    for right in range(n):
        rsum += 1 - nums[right]
        while k < rsum - lsum:
            lsum += 1 - nums[left]
            left += 1
        ans = max(ans, right - left + 1)
    return ans

