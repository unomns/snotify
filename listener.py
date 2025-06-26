
class Listener:
    def __init__(self, url, port):
        self.url = url
        self.port = port
    
    def listen(self):
        print(f"listening {self.url} on port {self.port}...")