class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self.Arr = [0 for i in range(capacity)]
        self.Start = 0
        self.End = 0
        self.Len = 0
        self.Cap = capacity

    def read(self):
        if(self.Len == 0):
            raise BufferEmptyException('Empty Buffer !')
        val = self.Arr[self.Start]
        self.Start = (self.Start+1)%self.Cap
        self.Len -= 1
        return val

    def write(self, data):
        if(self.Len == self.Cap):
            raise BufferFullException('Full Buffer !')
        self.Arr[self.End] = data
        self.End = (self.End+1)%self.Cap
        self.Len += 1

    def overwrite(self, data):
        if(self.Len == self.Cap):
            self.clear()
        self.write(data)

    def clear(self):
        if(self.Len > 0):
            self.Start = (self.Start+1)%self.Cap
            self.Len -= 1
