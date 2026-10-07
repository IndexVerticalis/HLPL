from datetime import datetime
class Logger:
    _instance = None
    _initialized = False

    VALID = {'DEBUG', 'INFO', 'WANR', 'ERROR', 'CRITICAL'}

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, path):
        if self._initialized:
            return
        self._initialized = True
        self.path = path

    def log(self, status, message):
        if status not in self.VALID:
            raise ValueError(f"Несуществующий статус: {status}")
        
        now = datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S')

        line = f"[{status}] {timestamp}: {message}"

        with open(self.path, 'a', encoding='utf-8') as f:
            f.write(line + '\n')

