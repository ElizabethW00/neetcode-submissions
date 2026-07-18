class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}
        for char in s:
            if char in dicts:
                dicts[char] += 1
            else:
                dicts[char] = 1
        dictt = {}
        for char in t:
            if char in dictt:
                dictt[char] += 1
            else:
                dictt[char] = 1
        print(dicts)
        print(dictt)
        return dicts == dictt