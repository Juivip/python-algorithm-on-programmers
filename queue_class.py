
import unittest


class MyStack(object):
    def __init__(self):
        self.lst = list()

    def push(self, x):
        self.lst.append(x)

    def pop(self):
        return self.lst.pop()

    def size(self):
        return len(self.lst)


class MyQueue(object):
    def __init__(self, max_size):
        self.stack1 = MyStack()
        self.stack2 = MyStack()
        self.max_size = max_size

    def qsize(self):
        return self.stack1.size()

    def push(self, item):
        if self.qsize() >= self.max_size:
            return False
        self.stack1.push(item)
        return True

    def pop(self):
        if self.stack1.size() == 0 :
            

        while self.stack1.size():
            self.stack2.push(self.stack1.pop())

        item = self.stack2.pop()

        while self.stack2.size():
            self.stack1.push(self.stack1.pop())
        return item

# n, max_size = map(int, input().strip().split(' '))
# print(n, max_size)


class Test(unittest.TestCase):
    def test(self):
        queue = MyQueue(1)

        self.assertEqual(queue.qsize(), 0)
        self.assertEqual(queue.push(3), True)
        self.assertEqual(queue.push(-5), False)
        self.assertEqual(queue.pop(), 3)
        self.assertEqual(queue.qsize(), 0)
        self.assertEqual(queue.pop(), False)


unittest.main()
