class Solution:
    def isValid(self, s: str) -> bool:
        mystack= []
        inverse= {'(':')', '{':'}', '[':']'}
        for char in s :
            if char in '({[':
                mystack.append(char)
                print("added",mystack)
            else:
                if len(mystack)==0 or inverse[mystack[-1]] != char:
                    print("char",char)
                    return False
                mystack.pop()
                print("removed",mystack)
        return len(mystack)==0