import unittest

from heapq import heappush, heappop
from random import randint

from heap import Heap


class TestHeap(unittest.TestCase):
    def setUp(self):
        self.heap = Heap()

    def test_heap_insert(self):
        list = [randint(1, 199) for _ in range(1000)]
        correct_heap = []
        for tuple in list:
            self.heap.insert(tuple)
            heappush(correct_heap, tuple)
        self.assertEqual(str(self.heap), str(correct_heap))

    def test_heap_is_empty(self):
        self.assertEqual(self.heap.is_empty(), True)

    def test_extract_when_heap_is_empty(self):
        self.assertEqual(self.heap.extract(), None)

    def test_extract_when_heap_is_not_empty(self):
        list = [(randint(1, 199), randint(1, 199)) for _ in range(1000)]
        correct_heap = []
        for tuple in list:
            self.heap.insert(tuple)
            heappush(correct_heap, tuple)
        for _ in range(1000):
            self.assertEqual(self.heap.extract(), heappop(correct_heap))
