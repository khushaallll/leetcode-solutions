def findMin(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        
        elif nums[mid] <= nums[right]:
            right = mid
        
        if mid == left == right:
            return nums[mid]
    

# nums = [2,1]
nums=[1,2,3,4]
# nums = [4, 5, 6, 7, 0, 1, 2]
print(findMin(nums))