def search(nums: list[int], target: int) -> int:
    
    left, right = 0, len(nums)-1 # initialize the pointers
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1

nums = [5]
target = 5
print(search(nums, target))