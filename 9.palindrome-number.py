#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x):
        normal = str(x)
        reverse = normal[::-1]
        return True if normal == reverse else False
# @lc code=end

