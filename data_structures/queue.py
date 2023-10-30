from linkedList import DoublyLinkedList


class Queue:
    def __init__(self):
        self.q = DoublyLinkedList()

    def __str__(self):
        return str(self.q)

    def isEmpty(self):
        return self.q.isEmpty()

    def enqueue(self, value):
        self.q.append(value)

    def dequeue(self):
        removed = self.q.removeFirst()
        if removed:
            return removed.value

        return removed
