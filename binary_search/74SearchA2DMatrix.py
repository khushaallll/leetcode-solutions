def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    left = 0
    right = len(matrix) * len(matrix[0]) - 1


    while left <= right:
        print("-----------------------")
        mid_idx = (left+right) // 2
        print(f"Left: {left} Right: {right}")
        print("mid_idx: ",mid_idx)

        # Find position of the mid element
        row = mid_idx//len(matrix[0])
        column = mid_idx % len(matrix[0])
        print(f"Row: {row} Column: {column}")
        # if row > len(matrix) -1 or column > len(matrix[0])-1:
        #     return False

        mid = matrix[row][column]
        print("Mid element: ",mid)
        if target == mid:
            return True
        
        if target > mid:
            left = mid_idx + 1
        else:
            right = mid_idx - 1
    
    return False



matrix = [[1,3]]
target = 3
print(searchMatrix(matrix, target))