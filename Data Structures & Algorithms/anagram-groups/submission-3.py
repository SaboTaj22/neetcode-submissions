class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # Map each letter-count signature to the list of words that share it

        for s in strs: # Iterate through each string in the input
            count = [0] * 26 # One counter for each letter a-z, all starting at 0
            for c in s: # Iterate through each character in the string
                count[ord(c) - ord("a")] += 1 # Convert the character to an index 0-25 and increment its count
            groups[tuple(count)].append(s) # Lists can't be dict keys, so convert to a tuple. Anagrams share the same counts, so they land in the same group

        return list(groups.values()) # Return all of the groups as a list of lists

        # Time Complexity: O(n * k)
        # Space Complexity: O(n * k)