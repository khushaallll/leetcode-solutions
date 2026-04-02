def cal_time(piles, speed):
    time = 0
    for pile in piles:
        hours = (pile + speed - 1) // speed
        time = time + hours 
    return time

def minEatingSpeed(piles: list[int], h: int) -> int:

    left = 1
    right = max(piles)

    while left <= right:
        print("\n")
        mid = (left + right) // 2
        total_time = cal_time(piles, mid)
        print(f"Left: {left} Mid: {mid} Right: {right} TotalTime: {total_time} ")
        if total_time <= h:
            right = mid - 1
        else:
            left = mid + 1
    
    return left

piles = [30,11,23,4,20]
h = 6
print(minEatingSpeed(piles, h))
