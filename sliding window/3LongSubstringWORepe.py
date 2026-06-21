# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

def lengthOfLongestSubstring(s: str) -> int:
    ### I wrote
    # left = 0
    # max_len_substring = 0
    # track_set = set()
    
    # for right in range(len(s)):
    #     if s[right] not in track_set:
    #         track_set.add(s[right])

    #     else:
    #         if len(track_set) > max_len_substring: # update the max length seen
    #             max_len_substring = len(track_set)
            
    #         while left < len(s): # move left until the valid window
    #             track_set.remove(s[left])
    #             if s[left] == s[right]:
    #                 left += 1
    #                 break
    #             left += 1

    #         track_set.add(s[right])

    #     if len(track_set) > max_len_substring:
    #         max_len_substring = len(track_set)
    
    # return max_len_substring

    ## chatgpt
    left = 0
    longest_ss = 0
    seen = set()

    for right in range(len(s)):
        while s[right] in seen: # window invalid
            seen.remove(s[left])
            left = left + 1

        seen.add(s[right])
        longest_ss = max(longest_ss, right - left + 1) # window valid - update answer
    
    return longest_ss

s = "hghyyhywhxhshss"
print(lengthOfLongestSubstring(s))