# Program to implement stack in python

# 1st way is using list data structure
stack = []
stack.append(2)
stack.append(3)
stack.append(5)

print(stack)
print('1st pop: ',stack.pop())
print('After 1st pop: ',stack)
print('2nd pop: ',stack.pop())
print('After 2nd pop stack: ',stack)

print('######## End of first implementation ########')

# 2nd way: using collection.deque class
# The deque (double-ended queue) class is optimized for append and pop operations from both ends, making it a more efficient choice for implementing a stack
from collections import deque
stack = deque()
stack.append(4)
stack.append(6)
stack.append(8)

print(stack)
print('1st pop: ',stack.pop())
print('After 1st pop: ',stack)
print('2nd pop: ',stack.pop())
print('After 2nd pop stack: ',stack)

print('######## End of second implementation ########')

# 3rd way implementing a Stack Class:
# For more control and clarity, you can create a custom stack class.
class Stack():
  def __init__(self):
    self.items = []
    
  def isempty(self):
    return len(self.items)==0

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if not self.items.isempty():
      return(self.items.pop())
      
  def peek(self):
        if not self.is_empty():
            return self.items[-1]

# Usage
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek())
print(stack.pop())
