from stack import Stack
import pytest


def test_empty_stack():
  stack = Stack()
  assert stack.is_empty() == True


def test_not_empty_stack():
  stack = Stack()
  stack.push('element 1')
  assert stack.is_empty() == False


def test_size_stack():
  stack = Stack()
  stack.push('element a')
  stack.push('element b')
  assert stack.size == 2


def test_push_pop_stack():
  stack = Stack()
  stack.push('element c')
  stack.push('element d')
  elem = stack.pop()
  assert elem == 'element d'
  elem = stack.pop()
  assert elem == 'element c'
  assert stack.is_empty() == True


def test_empty_stack_exception():
  stack = Stack()
  with pytest.raises(Exception):
    stack.pop()
