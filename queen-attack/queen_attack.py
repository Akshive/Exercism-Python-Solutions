class Queen(object):
    def __init__(self, row, column):
        if(row < 0 or column < 0 or row > 7 or column > 7):
            raise ValueError('Invalid Args')
        self.Row = row
        self.Column = column

    def can_attack(self, another_queen):
        if(self.Row == another_queen.Row and self.Column == another_queen.Column):
            raise ValueError('Invalid Args')
        if(self.Row == another_queen.Row or self.Column == another_queen.Column or (self.Row-self.Column == another_queen.Row-another_queen.Column) or (self.Row+self.Column == another_queen.Row+another_queen.Column)):
            return True
        return False
