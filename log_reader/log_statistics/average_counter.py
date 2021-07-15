class AverageCounter:
    def __init__(self):
        self.items_count = 0
        self.sum = 0

    def add(self, value) -> None:
        self.items_count += 1
        self.sum += value

    def average(self) -> float:
        try:
            average = self.sum / self.items_count
        except ZeroDivisionError:
            return 0.0
        return average
