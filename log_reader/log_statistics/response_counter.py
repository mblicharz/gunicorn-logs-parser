from collections import Counter


class ResponseCounter(Counter):
    def __init__(self):
        super().__init__()

    def get_output(self):
        output = ', '.join(f'{k}: {v}' for k, v in sorted(self.items()))
        return f'({output})'
