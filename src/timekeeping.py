import time

class Timer:
    def __init__(self, fps, seconds):
        self._tick_count = 0
        self._end_ticks = int(seconds * fps)
        self._completed = False
        self._fps = fps
        self._seconds = seconds

    @property
    def completed(self):
        return self._completed
    
    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    def seconds(self, seconds):
        self._seconds = seconds
    

    def tick(self):
        if not self._completed:
            self._tick_count += 1
            if self._tick_count == self._end_ticks:
                self._completed = True

    def reset(self):
        self._tick_count = 0
        self._completed = False
        self._end_ticks = int(self._seconds * self._fps)
        if self._end_ticks <= 0:
            self._end_ticks = 1


class Clock:
    def __init__(self, fps=60):
        self._fps = fps
        self._spf = 1 / fps
        self._start_time = time.time()

    @property
    def fps(self):
        return self._fps
    

    def tick(self):
        current_time = time.time()

        while current_time - self._start_time < self._spf:
            current_time = time.time()

        self._start_time = time.time()