class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res = [0] * len(temperatures)
        # stack = []
        
        # for index, temp in enumerate(temperatures):
        #     while stack and temp > stack[-1][0]:
        #         stackTemp, stackIndex = stack.pop()
        #         res[stackIndex] = (index- stackIndex)
        #     stack.append([temp, index])
        # return res

        temps = temperatures
        n = len(temps)
        res = [0] * n
        stack = []

        for i, t in enumerate(temps):
            while stack and stack[-1][0] < t:
                stack_t, stack_i = stack.pop()
                res[stack_i] = i - stack_i
            stack.append([t, i])
        return res