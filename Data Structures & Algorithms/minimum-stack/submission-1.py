class MinStack:

    def __init__(self):
        self.stack = []
        self.minNum = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.minNum = val
        else:
            self.stack.append(val-self.minNum)
            if self.minNum > val:
                self.minNum = val

    def pop(self) -> None:
        if not self.stack:
            return
        pop = self.stack.pop()
        if pop < 0:
            self.minNum = self.minNum-pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top +self.minNum
        else:
            return self.minNum

    def getMin(self) -> int:
        return self.minNum
