import functools
import time
from datetime import datetime
import json

class TimeIt:
    def __init__(self, func):
        self.func = func
        self.history = []
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        exc_type = None

        try:
            result = self.func(*args, **kwargs)
        except Exception as e:
            result = None
            exc_type = type(e).__name__
            raise
        finally:
            end = time.perf_counter()
            self.history.append({
                'name': self.func.__name__,
                'args': args,
                'kwargs': kwargs,
                'result': result,
                'exception': exc_type,
                'time': end - start,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
        return result

    def last(self):
        return self.history[-1] if self.history else None

    def count(self):
        return len(self.history)

    def clear(self):
        self.history.clear()

    def report(self):
        print(json.dumps(self.history, ensure_ascii=False, indent=4))
