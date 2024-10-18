# int binarySearch(int[] nums, int target) {
#     int left = 0, right = ...;
#
#     while(...) {
#         int mid = left + (right - left) / 2;
#         if (nums[mid] == target) {
#             ...
#         } else if (nums[mid] < target) {
#             left = ...
#         } else if (nums[mid] > target) {
#             right = ...
#         }
#     }
#     return ...;
# }

# 计算 mid 时需要防止溢出，代码中 left + (right - left) / 2 就和 (left + right) / 2 的结果相同，
# 但是有效防止了 left 和 right 太大，直接相加导致溢出的情况

# 主要问题包括while后不等号是否应该带等号，mid是否应该加一等

# 在sorted数组中寻找一个数
def binarySearch(nums, target: int) -> int:
    left = 0
    right = len(nums) - 1  # 注意，这里使用的是闭区间[left,right]

    while left <= right:  # 所以这里带等于号
        mid = left + (right - left) // 2  # 防止整型溢出
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1  # 注意 [left,right]
        elif nums[mid] > target:
            right = mid - 1  # 注意 [left,right]

    return -1


# 缺陷：[1,2,2,2,3]输出2
# 寻找左边界

def left_bound(nums, target: int) -> int:
    left = 0
    right = len(nums) - 1  # 注意

    while left <= right:  # 注意
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1  # 注意
    if left >= len(nums):
        return -1
    return left if nums[left] == target else -1


print(left_bound([1, 1, 2, 2, 2, 3], 2))


# 右边界
def right_bound(nums, target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # 这里改成收缩左侧边界即可
            left = mid + 1
    # 最后改成返回 left - 1
    # 由于 while 的结束条件为 right == left - 1，所以你把上述代码中的 left - 1 都改成 right 也没有问题
    # 这样可能更有利于看出来这是在「搜索右侧边界」
    if left - 1 < 0 or left - 1 >= len(nums):
        return -1
    return left - 1 if nums[left - 1] == target else -1


# lc 875
def minEatingSpeed(piles, h: int) -> int:
    small = 1
    big = max(piles)

    def try_(nums, k, h):
        cnt = 0
        for i in nums:
            cnt += i // k
            if i % k != 0:
                cnt += 1
        return cnt <= h

    while small <= big:
        mid = small + (big - small) // 2
        if try_(piles, mid, h):
            big = mid - 1
        else:
            small = mid + 1
    return small
