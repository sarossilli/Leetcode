class Logger:

    def __init__(self):
        self.msg = dict()
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.msg:
            self.msg[message] = timestamp
            return True
        elif self.msg[message] + 10 <= timestamp:
            self.msg[message] = timestamp
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)