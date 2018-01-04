import unittest
from Deque_Generator import get_deque, LL_DEQUE_TYPE, ARR_DEQUE_TYPE
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque(LL_DEQUE_TYPE)
    self.__stack = Stack()
    self.__queue = Queue()
    
    self.__deque1 = get_deque(ARR_DEQUE_TYPE)
    self.__stack1 = Stack()
    self.__queue1 = Queue()

  def test_empty_stack(self):
      self.assertEqual('[ ]', str(self.__stack), 'Empty stack(LL) should be printed as "[ ]"')
      self.assertEqual('[ ]', str(self.__stack1), 'Empty stack(ARR) should be printed as "[ ]"')
    
  def test_empty_queue(self):
      self.assertEqual('[ ]', str(self.__queue), 'Empty queue(LL) should be printed as "[ ]"')
      self.assertEqual('[ ]', str(self.__queue1), 'Empty queue(ARR) should be printed as "[ ]"')
      
  def test_push_stack_twice_then_pop(self):
      self.__stack.push(1)
      self.__stack.push(2)
      self.__stack.pop()
      self.assertEqual('[ 1 ]', str(self.__stack), 'Should print "[ 1 ]"')
      self.__stack1.push(1)
      self.__stack1.push(2)
      self.__stack1.pop()
      self.assertEqual('[ 1 ]', str(self.__stack1), 'Should print "[ 1 ]"')
      
  def test_enqueue_twice_then_dequeue(self):
        self.__queue.enqueue(-2)
        self.__queue.enqueue(5)
        self.__queue.dequeue()
        self.assertEqual('[ 5 ]', str(self.__queue), 'Should print "[ 5 ]"')
        self.__queue1.enqueue(-2)
        self.__queue1.enqueue(5)
        self.__queue1.dequeue()
        self.assertEqual('[ 5 ]', str(self.__queue1), 'Should print "[ 5 ]"')
   
  def test_pop_empty_stack(self):
      with self.assertRaises(IndexError):
          self.__stack.pop()
          self.__stack1.pop()
      self.assertEqual('[ ]', str(self.__stack), 'Should raise IndexError')
      self.assertEqual('[ ]', str(self.__stack1), 'Should raise IndexError')
      
  def test_dequeue_empty_queue(self):
      with self.assertRaises(IndexError):
          self.__queue.dequeue()
          self.__queue1.dequeue()
      self.assertEqual('[ ]', str(self.__queue))
      self.assertEqual('[ ]', str(self.__queue1))
      
  def test_length_of_stack(self):
      for i in range(3):
          self.__stack.push(i)
          self.__stack1.push(i)
      self.assertEqual(3, len(self.__stack), 'Length should be 3')
      self.assertEqual(3, len(self.__stack), 'Length should be 3')
  
  def test_length_of_queue(self):
      for i in range(5):
          self.__queue.enqueue(i)
          self.__queue1.enqueue(i)
      self.assertEqual(5, len(self.__queue), 'Length should be 5')
      self.assertEqual(5, len(self.__queue1), 'Length should be 5')
    
  def test_peek_stack(self):
      for i in range(10):
          self.__stack.push(i)
          self.__stack1.push(i)
      for j in range(3):
          self.__stack.pop()
          self.__stack1.pop()
      self.assertEqual(6, self.__stack.peek(), 'Top should be 6')
      self.assertEqual(6, self.__stack1.peek(), 'Top should be 6')
      
  def test_push_front_then_back_then_peek_front_and_back_then_pop(self):
      for i in range(10):
          if i%2 != 0:
              self.__deque.push_front(i)
              self.__deque1.push_front(i)
          else:
              self.__deque.push_back(i)
              self.__deque1.push_back(i)
      self.assertEqual('[ 9, 7, 5, 3, 1, 0, 2, 4, 6, 8 ]', str(self.__deque))
      self.assertEqual('[ 9, 7, 5, 3, 1, 0, 2, 4, 6, 8 ]', str(self.__deque1))
      self.assertEqual(9, self.__deque.peek_front(), 'Peek front should be 9')
      self.assertEqual(9, self.__deque1.peek_front(), 'Peek front should be 9')
      self.assertEqual(8, self.__deque.peek_back(), 'Peek back should be 8')
      self.assertEqual(8, self.__deque1.peek_back(), 'Peek back should be 8')
      for j in range(4):
          if j%2 != 0:
              self.__deque.pop_front()
              self.__deque1.pop_front()
          else:
              self.__deque.pop_back()
              self.__deque1.pop_back()
      self.assertEqual('[ 5, 3, 1, 0, 2, 4 ]', str(self.__deque))
      self.assertEqual('[ 5, 3, 1, 0, 2, 4 ]', str(self.__deque1))
      self.assertEqual(5, self.__deque.peek_front(), 'Peek front should be 5 after two pop_front')
      self.assertEqual(5, self.__deque1.peek_front(), 'Peek front should be 5 after two pop_front')
      self.assertEqual(4, self.__deque.peek_back(), 'Peek back should be 4 after two pop_back')
      self.assertEqual(4, self.__deque1.peek_back(), 'Peek back should be 4 after two pop_back')

      
if __name__ == '__main__':
  unittest.main()

