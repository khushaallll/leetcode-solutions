def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    
    total_ele = len(nums1) + len(nums2)
    n_left = total_ele // 2                  # number of elements needed on left of the partition
    inter = None
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    # binary search on partition
    left, right = 0, len(nums1)

    while left <= right:
        mid = (left + right) // 2            # mid partition

        max_left_nums1 = nums1[mid-1] if mid != 0 else float("-inf")
        min_right_nums1 = nums1[mid] if mid < len(nums1) else float("inf")

        surplus = n_left - mid
        max_left_nums2 = nums2[surplus-1] if surplus != 0 else float("-inf")
        min_right_nums2 = nums2[surplus] if surplus < len(nums1) else float("inf")

        if not max_left_nums1 <= min_right_nums2:
            # too many elements from nums1 and too less from nums2 on left
            # partition is on far right
            # partition needs to move left
            right = mid - 1
        
        elif not max_left_nums2 <= min_right_nums1:
            # too less elements from nums1 and too many from nums2 on left
            # partition is on far left
            # partition needs to move to right
            left = mid + 1
        else:
            if total_ele % 2 == 0: # even
                median = (max(max_left_nums1, max_left_nums2) + min(min_right_nums1, min_right_nums2)) / 2
            else:
                median = min(min_right_nums1, min_right_nums2)
            return median

nums1 = []
nums2 = [1]
print(findMedianSortedArrays(nums1, nums2))