class Solution(object):
    def isValid(self, s):
        openBrackets = ["(", "{", "["]
        closeBrackets = [")", "}", "]"]
        stack = []
        for i in range(len(s)):
            if s[i] in openBrackets:
                stack.append(s[i])
            else:
                top = ""
                if stack:
                    top = stack[-1]
                if s[i] == ")" and top == "(":
                    stack.pop()
                elif s[i] == "}" and top == "{":
                    stack.pop()
                elif s[i] == "]" and top == "[":
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True