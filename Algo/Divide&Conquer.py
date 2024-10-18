# merge_sort 代码实现

from typing import List

# 递归算法的时间复杂度本质上是要看: 递归的次数 * 每次递归中的操作次数
def merge(arr1: List[int], arr2: List[int]):
    result = []
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))
    if arr1:
        result += arr1
    if arr2:
        result += arr2
    return result


def merge_sort(arr: List[int]):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

# leetcode 241
def diffWaysToCompute(self, s: str) -> List[int]:
    # 如果只剩下数字，返回单个数值的列表
    if s.isdigit():
        return [int(s)]

    res = []
    # 迭代字符串，以符号分治
    for i in range(len(s)):
        if s[i] in "+-*":
            # 递归字符串前半部分和后半部分
            left = self.diffWaysToCompute(s[:i])
            right = self.diffWaysToCompute(s[i + 1:])
            # 组合两个结果的值
            for j in left:
                for k in right:
                    if s[i] == "+":
                        res.append(j + k)
                    elif s[i] == "-":
                        res.append(j - k)
                    elif s[i] == "*":
                        res.append(j * k)
    return res
