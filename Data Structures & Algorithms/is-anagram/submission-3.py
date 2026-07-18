class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ds = {}
        for i in s:
            ds[i] = ds.get(i, 0) + 1
        dt = {}
        for i in t:
            dt[i] = dt.get(i, 0) + 1

        return dt == ds
        