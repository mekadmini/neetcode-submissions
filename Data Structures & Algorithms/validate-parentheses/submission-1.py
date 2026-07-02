class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        for l in s:
            print(stack)
            if l in ["(", "[", "{"]:
                stack.append(l)
            else:
                match l:
                    case ")":
                        if stack and stack[-1] == "(":
                            stack.pop()
                        else:
                            return False
                    case "]":
                        if stack and stack[-1] == "[":
                            stack.pop()
                        else:
                            return False
                    case "}":
                        if stack and stack[-1] == "{":
                            stack.pop()
                        else:
                            return False
        return not stack

        