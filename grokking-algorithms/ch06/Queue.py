class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        if data not in self.queue:
            self.queue.append(data)
            return True
        return False

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return "No elements in Queue!"

    def size(self):
        return len(self.queue)


if __name__ == '__main__':
    my_queue = Queue()
    my_queue.enqueue("one")
    my_queue.enqueue("two")
    my_queue.enqueue("three")
    print(my_queue.size())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())

