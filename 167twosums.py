def twosums():
    numbers = [-1,0]
    target = -1

    left, right = 0, len(numbers) - 1

    while right > left:
        print(numbers[left], numbers[right])
        pos_tar = numbers[left] + numbers[right]
        if pos_tar != target:
            if pos_tar > target:
                right -= 1
            else:
                left += 1
        else: 
            return [left+1, right+1]

print(twosums())
        
