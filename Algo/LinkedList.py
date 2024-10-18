from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next  # 指向下一个node


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head

    while curr:
        holder = curr.next
        curr.next = prev
        prev = curr
        curr = holder

    return prev


def reverse(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    last = reverse(head.next)
    head.next.next = head
    head.next = None
    return last


a = ListNode(3)
b = ListNode(1)
c = ListNode(5)
d = ListNode(2)
e = ListNode(8)
a.next = b
b.next = c
c.next = d

# new = a
# a = e #不会改变new


temp = a
temp.next = e  # 同时改变a

# temp = a
# while temp:
#     temp = temp.next  # a不变 temp地址变了，不再指向a
# while a:
#     print(a.val)
#     a = a.next
