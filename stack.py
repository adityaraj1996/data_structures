class Stack:
    def __init__(self):
        self.stack = []

    def add(self, val):
        # Use list append method to add element
        if val not in self.stack:
            self.stack.append(val)
            return True

        else:
            return False

    def remove(self):
        if len(self.stack) == 0:
            print("the stack is empty")
            return False
        self.stack.pop()
        print(f"the modified stack is {self.stack}")
        return True


Stack_obj = Stack()
Stack_obj.add(23)
Stack_obj.add(24)
Stack_obj.add(25)
Stack_obj.add(26)
Stack_obj.remove()

