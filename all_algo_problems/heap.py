# Implementation of heap since I keep forgetting 
class Heap:
    def __init__(self, arr, mode):
        self.arr = arr
        self.mode = mode

    def build_heap(self): # Time complexity: O(n) 
        n = len(self.arr)
        start_index = (n//2)-1 # start from the non leaf node
        for i in range(start_index, -1, -1):
            if self.mode == 'max':
                self.max_heapify(i)
            else:
                self.min_heapify(i)

    def max_heapify(self, index): # Time complexity: O(logn)
        curr = index
        swap = True
        while self.left(curr) < len(self.arr) and swap:
            swap = False
            maxChild = self.findMaxChild(curr)
            if self.arr[maxChild] > self.arr[curr]:
                self.arr[curr], self.arr[maxChild] = self.arr[maxChild], self.arr[curr]
                swap = True
            curr = maxChild
        
    def min_heapify(self, index): # Time complexity: O(logn)
        curr = index
        swap = True
        while self.left(curr) < len(self.arr) and swap:
            swap = False
            minChild = self.findMinChild(curr)
            if self.arr[minChild] < self.arr[curr]:
                self.arr[curr], self.arr[minChild] = self.arr[minChild], self.arr[curr]
                swap = True
            curr = minChild

    def findMaxChild(self, index):
        left = self.left(index)
        right = self.right(index)   
        if right > len(self.arr):
            return left
        if self.arr[left] > self.arr[right]: return left
        else: return right     

    def findMinChild(self, index):
        left = self.left(index)
        right = self.right(index)   
        if right > len(self.arr):
            return left
        if self.arr[left] < self.arr[right]: return left
        else: return right 

    def parent(self, i):
        return (i-1)/2
    
    def left(self, i):
        return (2*i)+1
    
    def right(self, i):
        return (i+1)*2
    
    def add(self, val): # add any value
        # increase the value of heap
        # add value to the end of the heap
        # heapify again from non leaf node
        self.arr.append(val)
        start_index = (len(self.arr)//2) - 1
        if self.mode == 'max': self.max_heapify(start_index) # calling max heapify or min heapify --> hence O(logn)
        else: self.min_heapify(start_index)

    def remove(self): # deletes the root value
        # replace the root with the last element
        # reduce the size of the heap
        # heapify from root
        self.arr[0] = self.arr[len(self.arr)-1]
        self.arr.pop()
        if self.mode == 'max': self.max_heapify(0) # calling max heapify or min heapify --> hence O(logn)
        else: self.min_heapify(0)
        # if we want to remove a value by index, then we swap the index with the last element and heapify from the non leaf node again
        
    def __str__(self):
        return f"The resultant {self.mode} heap is {self.arr}."

# PRIORITY QUEUESSS
# Each data in a priority queue has a priority value to it
# The data with the highest priority is dequeued first
# If 2 elements have the same priority, they are served in the order in the queue
# When all elements are popped out of a priority queue, it will be in increasing/decreasing priority order
# There can be max/min priority queues --> These can be implemented using heap data structure
    # Time complexity of insertion/deletion in priority queues using heaps are O(logn)
        # Deletion usually deleted the highest or lowest priority depending on the application
    # Space complexity is usually dependent on the number of nodes/elements

# Priority queue using linked list
# Highest priority element is always at the head of the list
# Queue is arranged descending order of elements based on priority
# Removal of highest priority element will take O(1) time
# Insertion of element would require traversal through the list to find the appropriate place hence is O(n)
class PriorityQueueNode:
    def __init__(self, val, pr):
        self.val = val
        self.pr = pr
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def size(self):
        count = 0
        temp = self.head
        while temp.next:
            count += 1
            temp = temp.next

    def push(self, element, pr):
        newNode = PriorityQueueNode(element, pr)
        if self.isEmpty(): # check if queue is empty, if so, set the head of the queue as this new node
            self.head = newNode
        elif newNode.pr > self.head.pr: # if priority of this new node is more than the head, means it has the highest priority out of all the nodes
            temp = self.head
            self.head = newNode
            newNode.next = temp
        else:
            # if the new node priority is not more than the head priority, we need to traverse the queue to find the suitable place
            temp = self.head
            while temp.next != None:
                # if next node priority is lesser than the new node priority, new node will come after the next node
                if temp.next.pr < newNode.pr:
                    nextNode = temp.next
                    temp.next = newNode
                    newNode.next = nextNode
                    break # add break here since we are done adding 
                temp = temp.next # move on to the next node

    def pop(self):
        if self.isEmpty(): return "Empty"
        else:
            # update the head with the next node in queue
            self.head = self.head.next

    def peek(self):
        if self.isEmpty(): return "Empty"
        else:
            return self.head.val

# Python has a heapq modules, which by default is a min heap
import heapq

heap_arr = [1,3,2,9,4,5]
#heapq.heapify(heap_arr)# converting an iterable into a heap data structure

heapq.heappush(heap_arr, 11) # Push value onto heap while maintaining the heap invariant
print(heap_arr)
heapq.heappop(heap_arr) # Pop smallest value while maintaining the heap invariant 
heapq.heappushpop(heap_arr, 99) # push and then pop smallest item
heapq.heapreplace(heap_arr, 6) # replaces the popped item, but popped item may be larger than the item added

heapq.merge()

