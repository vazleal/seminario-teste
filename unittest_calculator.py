import unittest
from calculator import MemoryCalculator


class TestMemoryCalculator(unittest.TestCase):

  def test_sum_is_zero_on_initialization(self):
    calculator = MemoryCalculator()
    self.assertEqual(0, calculator.sum())

  def test_sum_one_number(self):
    calculator = MemoryCalculator()
    calculator.add(30)
    self.assertEqual(30, calculator.sum())

  def test_sum_two_numbers(self):
    calculator = MemoryCalculator()
    calculator.add(50)
    calculator.add(1)
    self.assertEqual(51, calculator.sum())
    calculator.add(3)
    calculator.add(2)
    self.assertEqual(5, calculator.sum())

  def test_sum_is_zero_after_calling_sum(self):
    calculator = MemoryCalculator()
    calculator.add(13)
    calculator.add(2)
    self.assertEqual(15, calculator.sum())
    self.assertEqual(0, calculator.sum())

  def test_sum_numbers_and_save_last_sum(self):
    calculator = MemoryCalculator(save_last_sum=True)
    calculator.add(5)
    calculator.add(10)
    self.assertEqual(15, calculator.sum())
    calculator.add(25)
    self.assertEqual(15, calculator.last_sum)
