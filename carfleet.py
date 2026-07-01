class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = zip(position, speed)
        cars = sorted(cars, reverse=True)
        stack = []
        for i , j in cars:
            time = float(target - i)/j
            if not stack or time> stack[-1]:
                stack.append(time)
             
        return len(stack)




        