class Node:

    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        if self.head is None and self.tail is None:
            self.tail = self.head = Node(data, None)
            return
        self.tail.next_node = Node(data, None)
        self.tail = self.tail.next_node

    def dequeue(self):
        if self.head is None:
            return None
        remove_data = self.head.data
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None
        return remove_data

    def __str__(self):
        l = []
        if self.head is None:
            return str(l)
        node = self.head
        while node:
            l.append(node.data)
            node = node.next_node
        return str(l)

    def to_list(self):
        l = []
        if self.head is None:
            return print(str(l))
        node = self.head
        while node:
            l.append(node.data)
            node = node.next_node
        return print(str(l))


if __name__ == "__main__":
    q = Queue()
    for i in range(10):
        q.enqueue(i)
        print(q)
    print(q.to_list)
    for i in range(4):
        q.dequeue()
        print(q)
