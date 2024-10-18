class treenode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inOrderTraversal(root):
    ans = []

    def inorder(root, ans):
        if not root:
            return None
        inorder(root.left, ans)  # adjust the order of three command lines to get preorder, postorder
        ans.append(root.val)
        inorder(root.right, ans)

    inorder(root, ans)
    return ans


def postOrderTraversal(root):
    ans = []

    def inorder(root, ans):
        if not root:
            return None
        inorder(root.left, ans)
        inorder(root.right, ans)
        ans.append(root.val)

    inorder(root, ans)
    return ans


def inOrderTraversalLoop(root):
    ans = []
    stack = []
    cur = root
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right
    return ans


def postOrderTraversalLoop(root):
    ans = []
    stack = []
    cur = root
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            node = stack[-1].right
            if not node:
                node = stack.pop()
                ans.append(node.val)
                while stack and stack[-1].right == node:
                    node = stack.pop()
                    ans.append(node.val)
            else:
                cur = node
    return ans


def postOrderIterative(root):
    # return if the tree is empty
    if root is None:
        return
    # create an empty stack and push the root node
    stack = [root]
    # create another stack to store postorder traversal
    out = []
    # loop till stack is empty
    while stack:
        # pop a node from the stack and push the data into the output stack
        curr = stack.pop()
        out.append(curr.val)
        # push the left and right child of the popped node into the stack
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    # print postorder traversal
    ans = [x for x in out if x]
    ans.reverse()
    return ans


a = treenode(1)
a.left = treenode(2)
a.left.left = treenode(3)
a.left.left.right = treenode(4)
a.right = treenode(5)
a.right.left = treenode(6)
a.right.right = treenode(9)
a.right.left.left = treenode(7)
a.right.left.left.right = treenode(8)

print(postOrderIterative(a))
