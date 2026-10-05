def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    median = None
    total_length = len(nums1) + len(nums2)
    n_left = total_length // 2              # elements supposed to be on left

    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    left, right = 0, len(nums1) # the mid is not going to be an index, it is suppose to be partition. so right starts at len(nums1) which is far right partition.
    
    while left <= right:

        mid = (left + right) // 2
        
        if mid > 0:
            max_left_nums1 = nums1[mid-1]
        else:
            max_left_nums1 = float("-inf") # if the partition is at extreme left [| 1, 3, 8, 9, 15]
        
        if mid > len(nums1):
            min_right_nums1 = float("inf") # if the partition is at extreme right [1, 3, 8, 9, 15 |]
        else:
            min_right_nums1 = nums1[mid]

        surplus = n_left - mid              # more elements needed from nums2 to be on left side of the partition

        max_left_nums2 = nums2[surplus-1] if surplus >= 0 else float("-inf")
        min_right_nums2 = nums2[surplus] if surplus < len(nums2) else float("inf")

        print(max_left_nums1, min_right_nums2)
        print(max_left_nums2, min_right_nums1)
        if max_left_nums1 >= min_right_nums2:
            print("ine here 1")
            right = mid - 1
        elif max_left_nums2 >= min_right_nums1:
            print("ine here 2")
            left = mid + 1
        else:
            if total_length % 2 != 0:
                median = min(min_right_nums1, min_right_nums2)
            else:
                median = (max(max_left_nums2, max_left_nums1) + min(min_right_nums1, min_right_nums2)) / 2
            return median

nums1 = [1,3,8,9,15]
nums2 = [7, 11, 18, 19, 21, 25]
print(findMedianSortedArrays(nums1, nums2))