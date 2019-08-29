class Node(object):
    def __init__(self, value, succeeding=None, previous=None):
        self.Value = value
        self.Prev = previous
        self.Next = succeeding


class LinkedList(object):
    def __init__(self):
        self.HeadFront = None
        self.HeadBack = None
        self.Len = 0

    def __len__(self):
        return self.Len

    def push(self, value):
        if(self.Len == 0):
            self.HeadFront = Node(value)
            self.HeadBack = self.HeadFront
        else:
            newNode = Node(value, None, self.HeadFront)
            self.HeadFront.Next = newNode
            self.HeadFront = newNode
        self.Len += 1

    def pop(self):
        val = self.HeadFront.Value
        self.HeadFront = self.HeadFront.Prev
        self.Len -= 1
        return val

    def unshift(self, value):
        if(self.Len == 0):
            self.HeadBack = Node(value)
            self.HeadFront = self.HeadBack
        else:
            newNode = Node(value, self.HeadBack, None)
            self.HeadBack.Prev = newNode
            self.HeadBack = newNode
        self.Len += 1

    def shift(self):
        val = self.HeadBack.Value
        self.HeadBack = self.HeadBack.Next
        self.Len -= 1
        return val
