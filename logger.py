import json
class Logger():
    def __init__(self):
        self.lijst = []

    def log(self, log):
        self.lijst.append(log)

    def toon_logger(self):
        for log in self.lijst:
            print(log)
    
    def write_Json(self):
        with open("HTML/logger.json", "w") as f:
            json.dump(self.lijst, f)