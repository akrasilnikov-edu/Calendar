import calendar
import datetime
from functools import total_ordering

@total_ordering 
class DayStruct(object):
    def __init__(self) -> None:
        self.date:datetime.date|None = None
        self.emotion = None
        self.description = None

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DayStruct):
            return NotImplemented
        if self.date is None or other.date is None:
            return self.date is other.date  # Both None or one None
        return int(datetime.datetime.combine(self.date, datetime.time.min).timestamp()) == \
               int(datetime.datetime.combine(other.date, datetime.time.min).timestamp())
    
    def __lt__(self, other):
        if not isinstance(other, DayStruct):
            return NotImplemented
        if self.date is None or other.date is None:
            return False
        return self.date < other.date