class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # If the lengths aren't the same, they can't be anagrams, return False
            return False
        
        return sorted(s) == sorted(t) #If we know the lengths are the same, sort the strings and compare. If they match, we have an anagram!

        