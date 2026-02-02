"""
Simple Stack Implementation
A basic stack data structure with push, pop, and peek operations
"""

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top of stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item"""
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self):
        """Return top item without removing"""
        return self.items[-1]
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items in stack"""
        return len(self.items)


def reverse_string(text):
    """Reverse a string using stack"""
    stack = Stack()
    
    for char in text:
        stack.push(char)
    
    reversed_text = ""
    while not stack.is_empty():
        reversed_text += stack.pop()
    
    return reversed_text


def is_balanced(expression):
    """Check if parentheses are balanced"""
    stack = Stack()
    opening = "({["
    closing = ")}]"
    
    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.peek() == opening[closing.index(char)]:
                stack.pop()
    
    return stack.is_empty()

#test comment
# Test the code
if __name__ == "__main__":
    # Test stack
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(f"Stack size: {s.size()}")
    print(f"Top item: {s.peek()}")
    
    # Test reverse
    print(f"Reversed: {reverse_string('hello')}")
    
    # Test balanced parentheses
    print(f"Balanced '(())': {is_balanced('(())')}")
    print(f"Balanced '({)}': {is_balanced('({)}')}")