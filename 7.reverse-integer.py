#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x):
        xlist = list(str(x))
        xlist.reverse()
        negative = False
        for char in xlist:
            if char == "0" and xlist.index(char) == len(xlist) - 1 and len(xlist) > 1:
                del xlist[xlist.index(char)]
            if char == "-":
                del xlist[xlist.index(char)]
                negative = True
        y = int("".join(xlist)) * -1 if negative else int("".join(xlist))
        return y if y < 2**31 and y > -2**31 else 0

# @lc code=end
