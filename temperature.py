class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        index = []
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            index.append(i)
            while index and temperatures[i]> temperatures[index[-1]]:
                old_index = index.pop()
                answer[old_index] = i - old_index
            index.append(i)
        return answer


            


        