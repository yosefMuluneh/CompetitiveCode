class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        theSubStr = ''
        length = 0
        longest =[]
        for i in range(len(s)):
            if s[i] not in theSubStr:
                theSubStr += s[i]
                length += 1
                longest.append(theSubStr)
            else:
                for j in range(len(theSubStr)):
                    if s[i] == theSubStr[j]:
                        theSubStr = theSubStr[j+1:]
                        length -= 1
                        break
                theSubStr += s[i]
                longest.append(theSubStr)
        maxLen = 0
        for ele in longest:
            if len(ele) > maxLen:
                maxLen = len(ele)
        return maxLen