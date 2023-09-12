import time


class Timer:
    def __init__(self) -> None:
        self.timer = time.time() * 1000

    def elapsed_ms(self) -> float:
        return time.time() * 1000 - self.timer

    def timestamp(self) -> str:
        return f"{self.elapsed_ms():03f}ms"
