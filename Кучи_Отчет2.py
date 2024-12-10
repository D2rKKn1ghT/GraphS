import sys

class max_heap: 
    def __init__(self, sizelimit):
        self.sizelimit = sizelimit
        self.cur_size = 0
        self.Heap = [0]*(self.sizelimit + 1)
        self.Heap[0] = sys.maxsize
        self.root = 1

    def swapnodes(self, node1, node2):
        self.Heap[node1], self.Heap[node2] = self.Heap[node2], self.Heap[node1]
 
    def max_heapify(self, i):
        left = 2 * i
        right = 2 * i + 1
        largest = i

        if left <= self.cur_size and self.Heap[left] > self.Heap[largest]:
            largest = left
        if right <= self.cur_size and self.Heap[right] > self.Heap[largest]:
            largest = right

        if largest != i:
            self.swapnodes(i, largest)
            self.max_heapify(largest)
 

    def heappush(self, element):
        if self.cur_size >= self.sizelimit :
            return
        self.cur_size+= 1
        self.Heap[self.cur_size] = element 
        current = self.cur_size
        while self.Heap[current] > self.Heap[current//2]:
            self.swapnodes(current, current//2)
            current = current//2
 
    def heappop(self):
        last = self.Heap[self.root]
        self.Heap[self.root] = self.Heap[self.cur_size]
        self.cur_size -= 1
        self.max_heapify(self.root)
        return last

    def build_heap(self): 
        for i in range(self.cur_size//2, 0, -1):
            self.max_heapify(i)
 
    def print_heap(self):
        for i in range(1, (self.cur_size//2)+1):
            print("Parent "+ str(self.Heap[i])+" Left Child is "+ str(self.Heap[2 * i]) +  " Right Child is "+ str(self.Heap[2 * i + 1]))
 
 

maxHeap = max_heap(10)
maxHeap.heappush(15)
maxHeap.heappush(7)
maxHeap.heappush(3)
maxHeap.heappush(33)
maxHeap.heappush(1000)
maxHeap.print_heap()
maxHeap.heappop()
maxHeap.print_heap()