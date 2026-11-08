class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        left = 0
        right = 0

        result = []

        while left < len(temperatures):

            current_temp = temperatures[left]
            exploring_temp = temperatures[right]
            
            while right < len(temperatures) and exploring_temp <= current_temp:

                exploring_temp = temperatures[right]               

                if exploring_temp > current_temp:
                    result.append(right - left)

                right+=1

            if exploring_temp <= current_temp:
                result.append(0)

            
            left+=1
            right = left

        return result

                
        