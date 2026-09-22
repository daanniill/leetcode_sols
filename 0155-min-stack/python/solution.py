    def top(self) -> int:
        return self.stack[-1][0]


        self.stack = self.stack[:-1]
    def pop(self) -> None:
            self.stack.append((value, min(value,self.stack[-1][1])))

            self.stack.append((value, value))
        else:
        if not self.stack:
    def push(self, value: int) -> None:

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
