class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If strings are not equal length, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Initialize hashmaps for both strings frequency counting
        s_freq = {}
        t_freq = {}

        # Build the frequency map for both strings simultaneously
        for s_char, t_char in zip(s,t):
            s_freq[s_char] = s_freq.get(s_char, 0) + 1
            t_freq[t_char] = t_freq.get(t_char, 0) + 1

        # If the resulting maps are not equal length, they cannot be anagrams
        if len(s_freq) != len(t_freq):
            return False

        # Loop over one of the maps
        for s_key in s_freq:
            # Check if the key is not in the other map
            # Or if the frequency is not the same for both strings 
            if s_key not in t_freq or s_freq[s_key] != t_freq[s_key]:
                return False
            
        return True
