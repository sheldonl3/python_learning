#括号匹配
class Solution:
    def IsValidExp(self, s):
        l = len(s)
        if l < 2:
            return False
        stack = []
        for i in range(l):
            if s[i] == '[':
                stack.append('[')
            if s[i] == '{':
                stack.append('{')
            if s[i] == '(':
                stack.append('(')
            if s[i] == ')':
                if len(stack) == 0:
                    return False
                if stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            if s[i] == ']':
                if len(stack) == 0:
                    return False
                if stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            if s[i] == '}':
                if len(stack) == 0:
                    return False
                if stack[-1] != '{':
                    print('sss')
                    return False
                else:
                    stack.pop()
        if stack != []:
            return False
        return True


if __name__ == '__main__':
    sx = Solution()
    print(sx.IsValidExp(''))
