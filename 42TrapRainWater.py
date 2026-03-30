height = [4,2,0,3,2,5]

# o(n) Space Complexity - Form two arrays
def trap(height: list[int]) -> int:
    water = 0
    prefix_arr = []
    suffix_arr = [0 for k in range(len(height))]

    for idx, val in enumerate(height):
        if idx == 0:
            prefix_arr.append(val)
            continue
        
        prefix_arr.append(max(prefix_arr[idx-1], val))

    for k in range(len(height)-1, -1, -1):
        if k == len(height)-1:
            suffix_arr[k] = height[k]
            continue
        suffix_arr[k] = max(suffix_arr[k+1], height[k])
    
    for idx, val in enumerate(height):
        water_level = min(prefix_arr[idx], suffix_arr[idx]) - val
        if water_level > 0:
            water = water + water_level
    
    return water

def trap2(height: list[int]) -> int:
    water = 0
    left, right = 0, len(height) - 1

    left_max = height[left]
    right_max = height[right]
    count = 0
    while left < right:
        if right_max >= left_max:
            water_level = left_max - height[left]
            if water_level > 0:
                water = water + water_level
        
            left += 1
            if height[left] > left_max:
                left_max = height[left]
        
        elif right_max < left_max:
            water_level = right_max - height[right]
            if water_level > 0:
                water = water + water_level
            
            right -= 1
            if height[right] > right_max:
                right_max = height[right]
        
    
    return water

print(trap2(height))