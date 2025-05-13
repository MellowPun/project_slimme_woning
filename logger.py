
class Logger():
    def __init__(self):
        self.lijst = []

    def log(self, log):
        self.lijst.append(log)

    def toon_logger(self):
        for log in self.lijst:
            print(log)