# 解决一个回溯问题，实际上就是遍历一棵决策树的过程，树的每个叶子节点存放着一个合法答案。
# 你把整棵树遍历一遍，把叶子节点上的答案都收集起来，就能得到所有的合法答案。
# 公式：
# result = []
# def backtrack(路径, 选择列表):  # 路径记录了已经做过的选择, 选择列表一般可以推出
#     if 满足结束条件:
#         result.add(路径)
#         return
#     for 选择 in 选择列表:
#         # 做选择
#         将该选择从选择列表移除
#         路径.add(选择)
#         backtrack(路径, 选择列表)
#         # 撤销选择
#         路径.remove(选择)
#         将该选择再加入选择列表


def letterCombinations(digits):
    if not digits:
        return []
    res = []
    n = len(digits)
    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    def backTrack(temp):
        if len(temp) == n:
            res.append(temp)
            return
        i = len(temp)
        for j in dic[digits[i]]:
            temp += j
            backTrack(temp)
            temp = temp[:-1]

    backTrack("")
    return res


# nums = [4,3,7,5,1] 无重复不能重复使用
def permute(nums):
    if not nums:
        return
    res = []
    n = len(nums)
    used = [0] * n

    # 我们这里稍微做了些变通，没有显式记录「选择列表」，而是通过 used 数组排除已经存在 temp_list 中的元素，从而推导出当前的选择列表：
    def backTrack(temp_list, visited):
        if len(temp_list) == n:
            res.append(list(temp_list))
            return
        for i in range(len(nums)):
            if visited[i]:
                continue
            else:
                temp_list.append(nums[i])
                visited[i] = 1
                backTrack(temp_list, visited)
                visited[i] = 0
                temp_list.pop()

    backTrack([], used)
    return res


# 子集/组合/排列
# 组合即为子集问题，即长度为k的子集
# 子集问题中，元素没有重复时仅需要考虑选择列表从哪开始即可避免重复
# 元素有重复时，要先对数据进行排序，然后进行剪枝
# 元素能重复使用时，子集问题中从i+1开始改成仍为i开始
# https://labuladong.github.io/algo/di-ling-zh-bfe1b/hui-su-sua-56e11/#%E5%AD%90%E9%9B%86-%E5%85%83%E7%B4%A0%E6%97%A0%E9%87%8D%E4%B8%8D%E5%8F%AF%E5%A4%8D%E9%80%89
