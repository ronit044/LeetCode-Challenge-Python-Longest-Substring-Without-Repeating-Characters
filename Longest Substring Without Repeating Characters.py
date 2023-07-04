def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = 0
        n = ""
        for i in range(len(s)):
            xyz = ""
            for j in range(i, len(s)):
                if s[j] not in xyz:
                    xyz += s[j]
                    if len(xyz) > m:
                        m = len(xyz)
                        n = xyz
                else:
                    break
        return(len(n))
