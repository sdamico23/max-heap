#Lab #12
#Due Date: 03/22/2019, 11:59PM
########################################
#                                      
# Name: Stephen D'Amico
# Collaboration Statement: I worked alone.          
#  
########################################



class MaxHeapPriorityQueue:
    '''
        >>> h = MaxHeapPriorityQueue()
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h.heap
        [10, 5]
        >>> h.insert(14)
        >>> h.heap
        [14, 5, 10]
        >>> h.insert(9)
        >>> h.heap
        [14, 9, 10, 5]
        >>> h.insert(2)
        >>> h.heap
        [14, 9, 10, 5, 2]
        >>> h.insert(11)
        >>> h.heap
        [14, 9, 11, 5, 2, 10]
        >>> h.insert(6)
        >>> h.heap
        [14, 9, 11, 5, 2, 10, 6]
        >>> h.parent(2)
        14
        >>> h.leftChild(1)
        9
        >>> h.rightChild(1)
        11
        >>> h.deleteMax()
        14
        >>> h.heap
        [11, 9, 10, 5, 2, 6]
        >>> h.deleteMax()
        11
        >>> h.heap
        [10, 9, 6, 5, 2]
    '''

    def __init__(self):
        self.heap=[]
        self.size = 0

    def __len__(self):
        return len(self.heap)


    def parent(self,index):
        if  (index > 1 and index <= self.size):
            return self.heap[((index-1)//2)]
        else:
            return None
        

    def leftChild(self,index):
        if (index >=1 and index*2+1 <= self.size):
            return self.heap[index*2-1]

        else: 
            return None


    def rightChild(self,index):
        if (index>= 1 and ((index*2)+2)<= self.size):
            return self.heap[(index*2)]
        else:
            return None
 

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]


    def insert(self,x):
        index = self.size 
        self.heap.append(x)
        while (index !=0):
            parent = (index-1)//2
            if self.heap[parent] < self.heap[index]: 
                self.swap(parent,index)
            index = parent
        self.size = self.size+1



    def max_heapify(self, n):
        left = n *2+1
        right = n*2+2
        large = n
        if (len(self.heap)-1) >= left and self.heap[large] <self.heap[left]:
            large = left
        if (len(self.heap)-1) >= right and self.heap[large] < self.heap[right]:
            large = right
        if (large != n):
            self.swap(large, n)
            self.max_heapify(large)





    def deleteMax(self):
        if len(self.heap) == 0:
            return None
        large = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.max_heapify(0)
        return large 


