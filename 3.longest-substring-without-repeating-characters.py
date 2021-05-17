#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s):
        sslist = []
        for i in range(len(s)):
            ss = []
            ss.append(s[i])
            for j in range(i + 1, len(s)):
                if s[j] in ss:
                    break
                else:
                    ss.append(s[j])
            sslist.append(len(ss))

        try:
            return max(sslist)
        except ValueError:
            return 0

# @lc code=end

