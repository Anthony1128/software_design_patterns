class singleton:
    def __init__(self, cls):
        self._cls = cls
        self._instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = self._cls(*args, **kwargs)
        return self._instance


@singleton
class Logger:
    def __init__(self):
        self.start = None

    def write(self, message):
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
