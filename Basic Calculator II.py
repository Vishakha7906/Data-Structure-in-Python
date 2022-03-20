class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # remove spaces
        s = s.replace(" ","")
        
        num = [] # list of numbers 
        ops = [] # list of operators
        
        # read numbers and operators from string
        i = 0
        n = ""
        while i < len(s):
            if '9'>= s[i] >= '0':
                n = n + s[i]
            else:
                num.append(int(n))
                n = ""
                ops.append(s[i])
            i+=1
        if len(n) != 0:
            num.append(int(n))
        
        # compute all the * and / operations
        i = 0
        while i < len(ops):
            if ops[i] == '*':
                num[i] = num[i] * num[i+1]
                num.pop(i+1)
                ops.pop(i)
            elif ops[i] == '/':
                num[i] = num[i] / num[i+1]
                num.pop(i+1)
                ops.pop(i)
            else:
                i += 1
        
        # compute all the + and - operations
        i = 0
        while i < len(ops):
            if ops[i] == '+':
                num[i] = num[i] + num[i+1]
                num.pop(i+1)
                ops.pop(i)
            elif ops[i] == '-':
                num[i] = num[i] - num[i+1]
                num.pop(i+1)
                ops.pop(i)
                
        
        return num[0]