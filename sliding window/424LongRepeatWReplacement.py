def characterReplacement(s: str, k: int) -> int:
    left = 0
    longest = 0
    freq_map = {}

    for right in range(len(s)):
        freq_map[s[right]] = freq_map.get(s[right], 0) + 1
        
        while (right - left + 1 - max(freq_map.values())) > k:
            freq_map[s[left]] = freq_map.get(s[left]) - 1
            left += 1

        longest = max(longest, right - left + 1)
    
    return longest



s = "ABABBCBBABB"
k = 2
print(characterReplacement(s,k))