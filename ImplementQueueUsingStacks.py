class MyQueue:

    def __init__(self):
        self.push_st = []
        self.pop_st = []
        

    def push(self, x: int) -> None:
        self.push_st.append(x)
        

    def pop(self) -> int:
        self.peek()
        return self.pop_st.pop()
        

    def peek(self) -> int:
        if not self.pop_st:
            while self.push_st:
                self.pop_st.append(self.push_st.pop())
        return self.pop_st[-1]
        

    def empty(self) -> bool:
        return not self.push_st and not self.pop_st


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2, param_3, param_4)