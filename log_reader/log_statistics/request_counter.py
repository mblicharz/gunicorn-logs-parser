from datetime import datetime


class RequestCounter:
    def __init__(self):
        self.count = 0

    def update(self, value) -> None:
        self.count += value

    def get_requests_per_second(
            self,
            from_date: datetime,
            to_date: datetime
    ) -> float:
        difference = (to_date - from_date).total_seconds()
        requests_per_second = self.count / difference
        return requests_per_second
