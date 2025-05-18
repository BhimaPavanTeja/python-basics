
class FileOpener:
    def __enter__(self):
        self.file = open("example.txt", "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Exception handled inside context: {exc_val}")
        self.file.close()
        return True  

def with_context_manager():
    try:
        with FileOpener() as f:
            f.write("Hello World\n")
            raise ValueError("Oops inside with block")
    except Exception as e:
        print("Outside catch:", e)

with_context_manager()
