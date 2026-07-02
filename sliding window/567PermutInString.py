def checkInclusion(s1: str, s2: str) -> bool:
    target_freq_map = {}
    for ele in s1:
        target_freq_map[ele] = target_freq_map.get(ele, 0) + 1
    
    target_len = len(s1)
    left = 0
    freq_map = {}

    for right in range(len(s2)):
        
        freq_map[s2[right]] = freq_map.get(s2[right], 0) + 1

        if (right - left + 1) == target_len:
            if target_freq_map == freq_map:
                return True
            
            freq_map[s2[left]] = freq_map.get(s2[left]) - 1
            if freq_map[s2[left]] <= 0:
                del freq_map[s2[left]]
            left += 1

    return False

s1 = "ab"
s2 = "eidboaoo"
print(checkInclusion(s1, s2))