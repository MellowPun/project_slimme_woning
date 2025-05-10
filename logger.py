class Logger():
    def __init__(self):
        self.lijst = []
    
    def add(self,apparaat_string):
        self.lijst.append(apparaat_string)

    def toon_logger(self):
        for log in self.lijst:
            print(log)
