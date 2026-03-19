from threading import Lock


class SingletonMeta(type):
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    start: str = None

    def __init__(self, start: str = None):
        self.start = start

    def write(self, message: str):
        if self.start:
            print(f"{self.start}: {message}")
        else:
            print(message)


logger1 = Logger()
logger1.start = "Logger1>"
print("Logger1:", logger1)
logger1.write("Hello, World!")

logger2 = Logger()
logger2.start = "Logger2>"
print("Logger2:", logger2)
logger1.write("Hello, World!")
