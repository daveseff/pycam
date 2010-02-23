list = ["DropCutter", "PushCutter", "Dimension"]
__all__ = list

from DropCutter import DropCutter
from PushCutter import PushCutter

class Dimension:
    def __init__(self, start, end):
        self.start = float(start)
        self.end = float(end)
        self.min = float(min(start, end))
        self.max = float(max(start, end))
        self.downward = start > end
        self.value = 0.0

    def check_bounds(self, value=None, tolerance=None):
        if value is None:
            value = self.value
        if tolerance is None:
            return (value >= self.min) and (value <= self.max)
        else:
            return (value > self.min - tolerance) and (value < self.max + tolerance)

    def shift(self, distance):
        if self.downward:
            self.value -= distance
        else:
            self.value += distance

    def set(self, value):
        self.value = float(value)

    def get(self):
        return self.value

