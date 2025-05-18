class Logger:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.log_file = "app.log"
        return cls._instance
    def write_log(self, message):
        with open(self.log_file, 'a') as f:
            f.write(message + '\n')
    
    def show_log(self):
        with open(self.log_file, 'r') as f:
            print(f.read())

logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)

logger1.write_log("First log entry.")
logger2.write_log("Second log entry.")

logger1.show_log()
