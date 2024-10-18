arr = [5, 2, 6, 4, 8, 1, 9, 3]
n = len(arr)
min_index = [-1] * n
stack = []
for i in range(n):
    while stack and arr[i] < arr[stack[-1]]:
        min_index[stack.pop()] = i
    stack.append(i)

print(min_index)  # 第一个在右边更小的数的index

# 在一个list中记录长度为k的subarray中的最大的index
k = 4
deq = [0]
ans = [0]
for i in range(1, n):
    if i > deq[0] + k - 1:  # Check whether left bound is still accessible or not
        deq.pop(0)
    while deq and arr[i] > arr[deq[-1]]:
        deq.pop()  # 小于dp[i]的都删了,因为都没用了
    deq.append(i)  # 更新deq
    ans.append(deq[0])
print(ans)