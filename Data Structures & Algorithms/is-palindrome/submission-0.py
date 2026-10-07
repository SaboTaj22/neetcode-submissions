class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1 # Two pointers, one at the start and one at the end of the string

        while l < r: # Keep going until the pointers meet or cross
            while l < r and not self.alphaNum(s[l]): # Move the left pointer forward past any non-alphanumeric characters
                l += 1
            while l < r and not self.alphaNum(s[r]): # Move the right pointer backward past any non-alphanumeric characters
                r -= 1
            if s[l].lower() != s[r].lower(): # Compare the characters, ignoring case. If they don't match, it's not a palindrome
                return False
            l, r = l + 1, r - 1 # Characters matched, so move both pointers inward
        return True # Every pair matched, so it's a palindrome

    def alphaNum(self, c): # Helper to check if a character is alphanumeric
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

        # Time Complexity: O(n)
        # Space Complexity: O(1)