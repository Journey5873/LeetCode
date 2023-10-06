class Solution(object):
    def isValid(self, s):
        openBrackets = ["(", "{", "["]
        closeBrackets = [")", "}", "]"]
        stack = []
        for c in s:
            if c in openBrackets:
                stack.append(c)
            else:
                top = ""
                if stack:
                    top = stack[-1]
                if c == ")" and top != "(" or \
                c == "}" and top != "{" or \
                c == "]" and top != "[":
                    return False
                stack.pop()
        if stack:
            return False
        return True