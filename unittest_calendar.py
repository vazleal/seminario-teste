import unittest
from calendar import Calendar


class TestCalendar(unittest.TestCase):

  def setUp(self):
    self.cal = Calendar()

  def test_calendar_first_letter(self):
    self.assertEqual('M', self.cal.formatweekday(0, 1))
    self.assertEqual('S', self.cal.formatweekday(6, 1))

  def test_calendar_center_width_3(self):
    self.assertEqual('Mon', self.cal.formatweekday(0, 3))
    self.assertEqual('Sun', self.cal.formatweekday(6, 3))

  def test_calendar_center_width_8(self):
    self.assertEqual('  Mon   ', self.cal.formatweekday(0, 8))
    self.assertEqual('  Wed   ', self.cal.formatweekday(2, 8))

  def test_calendar_full_width_10(self):
    self.assertEqual('  Monday  ', self.cal.formatweekday(0, 10))
    self.assertEqual('Wednesday ', self.cal.formatweekday(2, 10))
