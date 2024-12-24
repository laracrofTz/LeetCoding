# When do we use queues?
# Queue is used whenever we need to process data in the order they were added due to FIFO principle

# Different implementations of Queue in Python

# class implementation
class queue_class:
    def __init__(self):
        self.__queue = []
    
    def enqueue(self, element):
        self.__queue.append(element)
    
    def dequeue(self):
        return self.__queue.pop(0)
    
    def size(self):
        return len(self.__queue)
    
    def isEmpty(self):
        return self.size(self.__queue) == 0
    
# Queue from queue library
from queue import Queue
# def using_queueLib():
q = Queue() # if no args, max size will be infinite
q.put(1)
q.put(2)
q.put(3)
q.put(4)
print(q.qsize())
print(q)
print(q.get())
print(q.get())
print(q.qsize())
print(q)