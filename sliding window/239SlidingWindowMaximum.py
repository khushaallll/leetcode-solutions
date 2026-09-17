from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []
        dq = deque()

        for right in range(len(nums)):

            # 1. Remove the indices that are outside the window
            while dq and dq[0] < right - k + 1: # (anything with index < right - k + 1 is out of window )
                dq.popleft()
            

            # 2. Remove smaller elements from the back
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            # 3. Append the new element
            dq.append(right)

            #4. Once the first window is complete -> the front is the maximum
            if right >= k - 1:
                result.append(nums[dq[0]])

        return result
            
