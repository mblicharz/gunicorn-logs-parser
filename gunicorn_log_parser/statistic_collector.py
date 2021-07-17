from collections import Counter


class StatisticCollector:
    def __init__(self):
        self.lines = 0
        self.failures = 0
        self.requests = 0
        self._sum_response_length = 0
        self._responses = Counter()

    def add_line(self) -> None:
        self.lines += 1

    def add_failure(self) -> None:
        self.failures += 1

    def add_request(self) -> None:
        self.requests += 1

    def add_response(self, status_code: int) -> None:
        self._responses.update({status_code: 1})

    def get_responses(self) -> dict:
        return dict(sorted(self._responses.items()))

    def add_response_len(self, value: int) -> None:
        self._sum_response_length += value

    def average_response_len(self) -> float:
        try:
            avg = self._sum_response_length / self.requests
        except ZeroDivisionError:
            avg = 0

        return float("%.2f" % avg)
