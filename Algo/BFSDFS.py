# https://blog.csdn.net/qq_43540763/article/details/115144191
import collections
from collections import defaultdict

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
}


def BFS(gra, s):  # s表示开始结点，广度优先算法依靠队列
    queue = [s]  # BFS基于队列
    seen = [s]
    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = gra[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.append(w)
        print(vertex)


def DFS(gra, s):
    stack = [s]  # 栈
    seen = [s]
    while len(stack) > 0:
        vertex = stack.pop()
        nodes = gra[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.append(w)
        print(vertex)

    # DFS(graph, 'A')  # 起点任选


# Leetcode 1319 DFS
def makeConnected(n, connections):
    def dfs(network, visited, srcComputer):
        visited[srcComputer] = True
        for adjComputer in network[srcComputer]:
            if not visited[adjComputer]:
                dfs(network, visited, adjComputer)

    if len(connections) < n - 1:
        return -1
    network = [[] for _ in range(n)]
    for connection in connections:
        network[connection[0]].append(connection[1])
        network[connection[1]].append(connection[0])
    visited = [False] * n
    minOperations = 0
    for computer in range(n):
        if not visited[computer]:
            dfs(network, visited, computer)
            minOperations += 1
    return minOperations - 1


# BFS
def makeConnected2(n: int, connections) -> int:
    if len(connections) < n - 1:
        return -1

    adj_dict = defaultdict(list)
    for u, v in connections:
        adj_dict[u].append(v)
        adj_dict[v].append(u)

    visited = [False] * n

    def bfs(start):
        q = collections.deque()
        q.append(start)

        while q:
            curr = q.popleft()
            for v in adj_dict[curr]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)

    count = 0
    for i in range(n):
        if not visited[i]:
            count += 1
            bfs(i)
    return count - 1


# print(makeConnected(n=6, connections=[[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))


# Leetcode 200
def numIslands(grid):
    if not grid:
        return 0
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    return count


def dfs(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
        return
    grid[i][j] = '#'
    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)


def strokesRequired(picture):  # picture is a list of string
    m = len(picture)
    n = len(picture[0])
    visited = [[0] * n for _ in range(m)]
    count = 0

    def dfs(pic, i, j, target):
        if i < 0 or j < 0 or i >= len(pic) or j >= len(pic[0]) or pic[i][j] != target or visited[i][j]:
            return
        visited[i][j] = 1
        dfs(pic, i + 1, j, target)
        dfs(pic, i - 1, j, target)
        dfs(pic, i, j + 1, target)
        dfs(pic, i, j - 1, target)

    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                target = picture[i][j]
                dfs(picture, i, j, target)
                count += 1
    return count


# leetcode 576
def findPaths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    modulo = 1000000007
    dp = [[[-1] * (maxMove + 1) for _ in range(n)] for _ in range(m)]

    def dfs(a, b, left):
        if a < 0 or a >= m or b < 0 or b >= n:
            return 1
        if left == 0:
            return 0
        if dp[a][b][left] >= 0:
            return dp[a][b][left]
        result = 0
        result += dfs(a - 1, b, left - 1) % modulo
        result += dfs(a + 1, b, left - 1) % modulo
        result += dfs(a, b - 1, left - 1) % modulo
        result += dfs(a, b + 1, left - 1) % modulo
        result = result % modulo
        dp[a][b][left] = result
        return result

    return dfs(startRow, startColumn, maxMove)


# print(findPaths(2, 4, 3, 0, 1))
