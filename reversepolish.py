class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                if i == "+":
                    x = a + b
                elif i == "-":
                    x = a-b
                elif i == "*":
                    x = a*b
                else:
                    x = int(float(a)/b)
                stack.append(x)
        
        return stack.pop()
                    


        