height = [1,2,4,3]
left, right = 0, len(height)-1

max = 0
while right > left:
    width = right - left
    length = min(height[right], height[left])
    area = width * length
    if area > max:
        max = area
    
    if min(height[left+1], height[right]) > min(height[right-1], height[left]):
        left += 1
    else:
        right -= 1

print(max)