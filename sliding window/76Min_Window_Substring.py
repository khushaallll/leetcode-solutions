def minWindow(s: str, t: str) -> str:

    target_freq_map = {}
    freq_map = {}

    for letter in t:
        freq_map[letter] = 0
        target_freq_map[letter] = target_freq_map.get(letter, 0) + 1

    min_valid_length = len(s)

    left = 0
    required = len(target_freq_map)
    matched = 0
    min_valid_substring = ""

    for right in range(len(s)):
    
        if s[right] in target_freq_map:
            freq_map[s[right]] = freq_map.get(s[right]) + 1
            if freq_map.get(s[right]) == target_freq_map.get(s[right]):
                matched += 1

        while matched == required:

            current_valid_length = right - left + 1
            if current_valid_length <= min_valid_length:
                min_valid_length = current_valid_length
                min_valid_substring = s[left:right+1]

            if s[left] in target_freq_map:
                if freq_map.get(s[left]) == target_freq_map.get(s[left]):
                    matched = matched - 1
                freq_map[s[left]] = freq_map.get(s[left]) - 1
                left = left + 1
            else:
                left = left + 1
    return min_valid_substring


s = "ADOBECODEBANC"
t = "ABC"
s = "gxkvmymaztebptcdhquxemoowthbmzluwvpivdiuwoxmjzrqrmpyyemwxwylxlhtiwddcnyycvmnxeeoqtmqzbnzznkwyuriqulujjtnhfbejfubahsckhbjwnfwhweaspubbnpivsogxiizrcbdjemfstdzrhzjwwnzjehgwxnvivwzzadkerpyluyebzozxdzhjipficcqzyryauifozdbtdfwfvwcyxlhhbopfsfhtxfttqahrginlqjslhxkektonkdtcjavihrdxrnrxxejnndzvajblepyqvrtgtqobhtabgraevjrlpqipbjaibzyystemkuptnruujvaggrrvkznnlnvoowmjpsxbmmvbdrxooxxxrqudshqfxotnkhwzztbnfyqlpobgladerzhjjyogojtyssxtlagtywgqmhwyibezamkjmarajnabfxuqacjyaponzmnhnriofuzturvfevgjvczvglviamvzykimesalmbfisanwyvhtxjqfulowxlwyygkczmnnnuwixjgvfoqexgmttaptnnrludpvpfiezemwqttxjjbirnblpqgfgzqacixtnfxmmmlefebqoeyfuzsjryqxzjzbrwweeusqgdunixdybddv"
t = "eyhvyxvygwb"
print(minWindow(s,t))