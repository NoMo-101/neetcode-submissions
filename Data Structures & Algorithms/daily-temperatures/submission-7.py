class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures
        res = [0] * len(temps)
        stack = []

        for index, temp in enumerate(temps):
            while stack and temp > stack[-1][0]:
                prev_t, prev_i = stack.pop()
                res[prev_i] = index - prev_i
            stack.append([temp, index])
        return res