nums = [4,5,6,7,0,1,2]
target = 5

def search(nums: list[int], target: int) -> int:
    
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        if nums[mid] <= nums[right]:
            # right sorted
            if nums[mid] < target < nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        
        elif nums[mid] >= nums[left]:
            if nums[mid] > target > nums[left]:
                right = mid - 1
            else:
                left = mid + 1
    
    return -1

print(search(nums, target))