#Author : Shivansh Anand
#Code for toy TCP stream receiver and reader
#NOTE : Code is incomplete


class ToyTCPStream:
    data = {}
    max_chunk = 0

    def receive(self, chunk, data):
        self.data[str(chunk)] = data
        if chunk > self.max_chunk:
            self.max_chunk = chunk

    def read(self, data):
        data = []
        if "1" not in self.data:
            return 0
        for i in range(1, self.max_chunk + 1):
            if str(i) in self.data:
                for j in self.data[str(i)]:
                    data.append(j)
        return len(data)

