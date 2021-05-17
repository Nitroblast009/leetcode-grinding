#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        sum = self.lltoNum(l1) + self.lltoNum(l2)
        res = [int(d) for d in str(sum)]
        res.reverse()
        llres = ListNode(res[0])
        prevNode = llres
        for d in res[1:]:
            currentNode = ListNode(d)
            prevNode.next = currentNode
            prevNode = currentNode
        return llres

    def lltoNum(self, l1):
        list1 = []
        node = l1
        while node:
            list1.append(node.val)
            node = node.next
        list1.reverse()
        num1 = [str(i) for i in list1]
        num1 = int("".join(num1))
        return num1
# @lc code=end

