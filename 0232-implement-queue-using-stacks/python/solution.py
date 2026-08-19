
    def pop(self) -> int:

    def peek(self) -> int:
        if not self.s2:
        return self.s2.pop()

    def empty(self) -> bool:
        return max(len(self.s1), len(self.s2)) == 0

    def push(self, x: int) -> None:

        self.s2 = []
        self.s1 = []
    def __init__(self):

class MyQueue:
        if not self.s2:
            for i in range(len(self.s1)):
                self.s2.append(self.s1.pop())
        self.s1.append(x)
            for i in range(len(self.s1)):
                self.s2.append(self.s1.pop())
        return self.s2[-1]
