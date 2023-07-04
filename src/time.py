

class Timer:
    def __init__(self, fps, seconds):
        self._tick_count = 0
        self._end_ticks = seconds * fps - 1
        self._completed = False

    @property
    def completed(self):
        return self._completed
    

    def tick(self):
        if not self._completed:
            self._tick_count += 1
            if self._tick_count == self._end_ticks:
                self._completed = True

    def reset(self):
        self._tick_count = 0
        self._completed = False