import time

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


class Clock:
    def __init__(self, fps=60):
        self._fps = 1 / fps
        self._start_time = time.time()

    def tick(self):
        current_time = time.time()

        while current_time - self._start_time < self._fps:
            current_time = time.time()

        self._start_time = time.time()