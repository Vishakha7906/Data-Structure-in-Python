class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True
        char_map, stack={'(':')','{':'}','[':']'},[]
        for e in s:
            if not stack or stack[-1] not in char_map or char_map[stack[-1]] != e:
                stack.append(e)
            else:
                stack.pop()
        return True if not stack else False