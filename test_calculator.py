from calculator import MemoryCalculator
import pytest

def test_sum_is_zero_on_initialization():
  calculator = MemoryCalculator()
  assert calculator.sum() == 0


def test_sum_one_number():
  calculator = MemoryCalculator()
  calculator.add(30)
  assert calculator.sum() == 30


def test_sum_two_numbers():
  calculator = MemoryCalculator()
  calculator.add(50)
  calculator.add(1)
  assert calculator.sum() == 51
  calculator.add(3)
  calculator.add(2)
  assert calculator.sum() == 5

@pytest.mark.parametrize("num1, num2, result", [(13,2,15), (10,1,11)])
def test_sum_is_zero_after_calling_sum(num1, num2, result):
  calculator = MemoryCalculator()
  calculator.add(num1)
  calculator.add(num2)
  assert calculator.sum() == result
  assert calculator.sum() == 0


def test_sum_numbers_and_save_last_sum():
  calculator = MemoryCalculator(save_last_sum=True)
  calculator.add(5)
  calculator.add(10)
  assert calculator.sum() == 15
  calculator.add(25)
  assert calculator.last_sum == 15
