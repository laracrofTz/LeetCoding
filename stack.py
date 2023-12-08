# When do we use Stack?
# When we want to keep track of previous actions or states, LIFO principle

# Different implementations of Stack in Python

# Using python List data type
def using_list():
    stack = []
    stack.append(9)
    stack.append(10)
    stack.pop()
    print(stack[-1])
    print(len(stack))

# OOP
class Stack:
    def __init__(self):
        self.__stack = [] # name mangling
    
    def __len__(self):
        return len(self.__stack)
    
    def isEmpty(self):
        if len(self.__stack) == 0:
            return True
        else:
            return False
        
    def push(self, element):
        self.__stack.append(element)

    def pop(self):
        if self.isEmpty() == True:
            raise Exception("List is empty")
        self.__stack.pop()
    
    def peek(self):
        if self.isEmpty() == True:
            raise Exception("List is empty")
        return self.__stack[-1]

    def __str__(self):
        return str(self.__stack)

# Queue module, LIFO queue
from queue import LifoQueue
def using_queueLib():
    stack = LifoQueue(2)
    stack.put(9)
    stack.put(10)
    # stack.put(11) # blocking call, waits until stack has an empty slot
    # stack.put_nowait(11) # non blocking, will raise an exception that queue is full
    print(stack.get())
    print(stack.qsize())
    print(stack.empty())
    print(stack.full())

# using singly linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack_LL:
    def __init__(self):
        self.head = Node("head")
        self.size = 0
    
    def getSize(self):
        return self.size
    
    def empty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.head.next
        self.head.next = newNode
        self.size += 1
    
    def pop(self):
        if self.empty() == True:
            raise Exception("Stack is empty")
        removeNode = self.head.next
        self.head.next = removeNode.next
        removeNode.next = None
        return removeNode.val
    
    def peek(self):
        if self.empty() == True:
            raise Exception("Stack is empty")
        return self.head.next.val