class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        x=""
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if(s[j-1]==s[j]):
                    break
                elif(s[j] in x):
                    break
                else:
                    x=s[i:j+1]
        if(x==""):
            return 1
        else:
            return len(x)
