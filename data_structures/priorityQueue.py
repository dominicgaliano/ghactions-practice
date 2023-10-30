class PQueue:
    def __init__(self):
        self.heap = []
        self.heapSize = 0

    def __str__(self):
        return str(self.heap)

    def isEmpty(self):
        return self.heapSize == 0

    def clear(self):
        self.heap = []

    def heapify(self):
        """O(n) efficient heap formation"""
        raise NotImplementedError("Not implemented for time sake")

    def size(self):
        return self.heapSize

    def peek(self):
        if self.isEmpty():
            return None
        return self.heap[0]

    def poll(self):
        return self.removeAt(0)

    def contains(self, element):
        for heapElement in self.heap:
            if element == heapElement:
                return True
        return False

    def removeAt(self, index):
        if index >= self.size():
            raise IndexError("index out of bounds")

        # need to deal with case of one element in heap
        if self.heapSize == 1:
            self.clear()
            return

        self.swap(index, self.size() - 1)
        removedElement = self.heap.pop()
        self.heapSize -= 1

        # WilliamFiset implementation:
        if index == self.heapSize:
            return removedElement

        element = self.heap[index]
        # try sinking
        self.sink(index)

        # if sinking did not work, try swimming
        if self.heap[index] == element:
            self.swim(index)

        # My original implementation:
        # left = 2 * index + 1
        # right = 2 * index + 2
        # parent = index // 2
        # if index == 0:
        #     self.sink(index)
        # elif self.less(index, parent):
        #     self.swim(index)
        # elif (right < self.heapSize and self.less(right, index)) or (
        #     left < self.heapSize and self.less(left, index)
        # ):
        #     self.sink(index)

        return removedElement

    def add(self, element):
        if element is None:
            raise TypeError("Element cannot be None")

        self.heap.append(element)
        self.swim(self.heapSize)
        self.heapSize += 1

    def swim(self, k):
        # bottom up node swim, O(log(n))
        parent = (k - 1) // 2
        while k > 0 and self.less(k, parent):
            # bubble up
            self.swap(k, parent)
            k = parent

            # recalculate parent
            parent = (k - 1) // 2

    def sink(self, k):
        # top down node sink, O(log(n))
        # ties sink to left
        while True:
            left = 2 * k + 1
            right = 2 * k + 2
            smallest = left

            if right < self.heapSize and self.less(right, left):
                smallest = right

            if left >= self.heapSize or self.less(k, smallest):
                break

            self.swap(smallest, k)
            k = smallest

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def less(self, i, j):
        return self.heap[i] <= self.heap[j]

    def remove(self, element):
        if element is None:
            raise TypeError("Element cannot be None")

        for i in range(self.size()):
            if self.heap[i] == element:
                return self.removeAt(i)
