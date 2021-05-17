#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s):
        intVal = 0
        i = 0
        while i < len(s):
            print(f"i starts at: {i}")
            if s[i] == "M":
                intVal+=1000
            elif s[i] == "D":
                intVal+=500
            elif s[i] == "C":
                try:
                    if s[i+1] == "M":
                        intVal+=900
                        i+=1
                    elif s[i+1] == "D":
                        intVal+=400
                        i+=1
                    else:
                        intVal += 100
                except IndexError:
                    intVal+=100
            elif s[i] == "L":
                intVal+=50
            elif s[i] == "X":
                try:
                    if s[i+1] == "C":
                        intVal+=90
                        i+=1
                    elif s[i+1] == "L":
                        intVal+=40
                        i+=1
                    else:
                        intVal+=10
                except IndexError:
                    intVal+=10
            elif s[i] == "V":
                intVal+=5
            else:
                try:
                    if s[i+1] == "X":
                        intVal+=9
                        i+=1
                    elif s[i+1] == "V":
                        intVal+=4
                        print(f"i+=1d i: {i}")
                        i+=1
                    else:
                        intVal+=1
                except IndexError:
                    intVal+=1
            i+=1
        return intVal
# @lc code=end

