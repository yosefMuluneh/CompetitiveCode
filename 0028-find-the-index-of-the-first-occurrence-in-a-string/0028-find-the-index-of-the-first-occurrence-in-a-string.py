class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle  not in haystack:
            return -1
        else:
            for i in range(0,len(haystack)):
                if haystack[i:i+len(needle)]==needle:
                    return i