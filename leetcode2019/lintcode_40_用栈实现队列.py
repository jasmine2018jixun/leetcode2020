
# 栈是先进后出，队列时先进先出的。
# 如果把元素放到stack1中，然后再把这些元素从stack1中弹出，依次放入stack2中，
# 然后取stack2中的元素，就可以实现先进先出了

# method 1: use build in pop and append
import Stack 

class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def push(self, elem):
        return self.in_stack.append(elem)
    
    def pop(self): # remove
        self.outSafe()
        return self.out_stack.pop()

    def top(self): # 不remove
        self.outSafe()
        return self.out_stack[-1]
    
    def outSafe(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) != 0:
                self.out_stack.append(self.in_stack.pop())

# method 2: not use build in pop and append, implement with list
class MyQueue:
    def __init__(self):
        self.in_stack, self.out_stack, self.out_index = [], [], -1

    def push(self, elem):
        self.in_stack += [elem]
    
    def pop(self):
        res, self.out_index = self.top(), self.out_index - 1
        return res
    
    def top(self):
        self.outSafe()
        return self.out_stack[self.out_index]

    def outSafe(self):
        if self.out_index == -1:
            self.out_stack, size = [], len(self.in_stack)
            for i in range(size):
                self.out_stack.append(self.in_stack[size - i - 1])
            self.in_stack, self.out_index = [], len(self.out_stack) - 1