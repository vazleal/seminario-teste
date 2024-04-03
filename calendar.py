class Calendar:

    _days = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
        'Sunday'
    ]

    def _weekday(self, index):
        return self._days[index]

    def formatweekday(self, day_index, width):
        if width <= 3:
            return self._weekday(day_index)[0:width]

        if width <= 8:
            return self._weekday(day_index)[0:3].center(width)

        return self._weekday(day_index).center(width)