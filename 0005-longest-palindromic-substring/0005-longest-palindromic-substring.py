class Solution(object):
    def longestPalindrome(self, s):
        longest = []
        if s == s[::-1]:
            return s
        else:
            for j in range(len(s)-1):
                for i in range(2,len(s)-j+1):
                    theSlice = s[j:j+i]
                    if theSlice == theSlice[::-1]:
                        longest.append(theSlice)
        if len(longest) ==0:
            return s[0]
        maxPal = 0
        thePal = ''
        for ele in longest:
            if len(ele) > maxPal:
                maxPal = len(ele)
                thePal = ele
        
        return thePal