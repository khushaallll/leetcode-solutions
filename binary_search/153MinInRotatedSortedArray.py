def findMin(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        
        print(f"left: {left} mid:{mid} right:{right}")
        print(f"left: {nums[left]} mid:{nums[mid]} right:{nums[right]}")
        
        if nums[mid] <= nums[left]:
            right = mid - 1
            print(f"Right updated = {right}")
        
        elif nums[mid] > nums[right]:
            left = mid + 1
            print(f"Left updated = {right}")
        
        else:
            return nums[left]
        
        print(f"left: {left} mid:{mid} right:{right}")
        print(f"left: {nums[left]} mid:{nums[mid]} right:{nums[right]}\n---------------")
    
    return nums[mid]


nums = [2,1]
# nums=[1,2,3,4]
print(findMin(nums))