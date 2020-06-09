class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def fullStackView(self):
        return self.items
# stack=Stack()
# print(stack.isEmpty())
# stack.push(7)
# stack.push(5)
# stack.push(89)
# stack.push(12)
# print(stack.fullStackView())
# print(stack.pop())
# print(stack.fullStackView())
# print(stack.isEmpty())
def paranthesis(str):
    stack = Stack()
    paraOpens,paraClose="<[{(", ">]})"
    for c in str:
        if c in paraOpens:
            stack.push(c)
            #print(stack.fullStackView())
        elif c in paraClose:
            if stack.isEmpty():
                return False
            else:
                stacktop=stack.pop()
                bracketBalance =paraOpens[paraClose.index(c)]
                #print(stacktop,",",bracketBalance)
                #print(stack.fullStackView())
                if stacktop != bracketBalance:
                    return False
                else:
                    if not stack.isEmpty():
                        continue
                    else:
                        return True
        else:
            continue


a = paranthesis("[[[[]]]]")
if a != None:
    print(a)
else:
    print(False)

