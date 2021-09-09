#Author : Shivansh Anand
#Code for toy TCP stream receiver and reader


class ToyTCPStream:
    data = {}
    max_chunk = 0

    def receive(self, chunk, data):
        self.data[str(chunk)] = data
        if chunk > self.max_chunk:
            self.max_chunk = chunk

    def read(self, data):
        if "1" not in self.data:
            return 0
