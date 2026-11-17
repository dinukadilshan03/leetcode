class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = {}
        for letter in s:
            if letter not in tracker:
                tracker[letter] = 1
            else:
                tracker[letter] +=1
        for letter in t:
            if letter not in tracker:
                return False
            else:
                tracker[letter] -=1
        if (all(count ==0 for count in tracker.values())):
            return True
        else:
            return False

        