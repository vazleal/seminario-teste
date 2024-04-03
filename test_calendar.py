from calendar import Calendar


def test_calendar_first_letter():
  cal = Calendar()
  assert cal.formatweekday(0, 1) == 'M'
  assert cal.formatweekday(6, 1) == 'S'


def test_calendar_center_width_3():
  cal = Calendar()
  assert cal.formatweekday(0, 3) == 'Mon'
  assert cal.formatweekday(6, 3) == 'Sun'


def test_calendar_center_width_8():
  cal = Calendar()
  assert cal.formatweekday(0, 8) == '  Mon   '
  assert cal.formatweekday(2, 8) == '  Wed   '


def test_calendar_full_width_10():
  cal = Calendar()
  assert cal.formatweekday(0, 10) == '  Monday  '
  assert cal.formatweekday(2, 10) == 'Wednesday '
