def largestRectangleArea(heights: list[int]) -> int:
    max_area = 0
    idx_stack = []
    heights.append(0) # to resolve all the areas in the end (minimum bar must be resolved as well)

    for idx, curr_h in enumerate(heights):
        while idx_stack and heights[idx_stack[-1]] > curr_h:
            height_idx = idx_stack.pop()

            #index of right smallest tower
            right_smallest_tower_idx = idx

            # index of left smallest tower
            left_smallest_tower_idx = -1 if not idx_stack else idx_stack[-1]
  
            width = right_smallest_tower_idx - left_smallest_tower_idx - 1 # -1 because we include index of left smallest tower as well so we subtract that
   
            area = heights[height_idx] * width
            if area > max_area:
                max_area = area
        
        idx_stack.append(idx)
    return max_area

heights = [2,1,5,6,2,3]
print(largestRectangleArea([2,4]))