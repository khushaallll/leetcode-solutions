class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0 for k in range(len(temperatures))]
        stack = []

        for idx, value in enumerate(temperatures):
            while stack and value > temperatures[stack[-1]]:
                eli = stack.pop()
                answer[eli] = idx - eli
            
            stack.append(idx)
        return answer
    
cl = Solution()
print(cl.dailyTemperatures(temperatures=[30,40,50,60]))