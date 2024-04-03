import unittest
from stack import Stack


class TestStack(unittest.TestCase):

  def setUp(self):
    self.stack = Stack()

  def testEmptyStack(self):
    self.assertTrue(self.stack.is_empty())

  def testNotEmptyStack(self):
    self.stack.push('element 1')
    self.assertFalse(self.stack.is_empty())

  def testSizeStack(self):
    self.stack.push('element a')
    self.stack.push('element b')
    self.assertEqual(2, self.stack.size)

  def testPushPopStack(self):
    self.stack.push('element c')
    self.stack.push('element d')
    elem = self.stack.pop()
    self.assertEqual(elem, 'element d')
    elem = self.stack.pop()
    self.assertEqual(elem, 'element c')
    self.assertTrue(self.stack.is_empty())

  def testEmptyStackException(self):
    with self.assertRaises(Exception):
      self.stack.pop()
