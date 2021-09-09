#Author : Shivansh Anand
#Code for toy TCP stream receiver and reader


class ToyTCPStream:
    data = {}
    
    def receive(self, chunk, data):
        self.data[str(chunk)] = data

    def read(self, data):
        pass
