class Custom_Exception(Exception):
    pass

class BowlingGame(object):
    def __init__(self):
        self.Arr = []
        for i in range(10):
            self.Arr.append([[], -1])
        self.frames = 0
        
    def roll(self, pins=-1):
        if(self.frames == 10):
            raise Custom_Exception('Bowling Game has only 10 frames.')
        if(pins < 0):
            raise Custom_Exception('pins can\'t be negative.')
        if(pins > 10):
            raise Custom_Exception('pins can\'t be more than 10.')
            
        self.Arr[self.frames][0].append(pins)
        
        if(self.frames == 9):
            if(len(self.Arr[self.frames][0]) == 2):
                if(self.Arr[9][0][0] < 10 and pins+self.Arr[9][0][0] > 10):
                    raise Custom_Exception('Invalid')
                if(pins + self.Arr[self.frames][0][0] < 10):
                    self.frames += 1
            elif(len(self.Arr[self.frames][0]) == 3):
                if((self.Arr[9][0][0] == 10 and self.Arr[9][0][1] < 10) and (self.Arr[9][0][1]+self.Arr[9][0][2] > 10)):
                    raise Custom_Exception('Invalid Args')
                self.frames += 1
        else:
            if(len(self.Arr[self.frames][0]) == 2):
                if(pins + self.Arr[self.frames][0][0] < 10):
                    self.Arr[self.frames][1] = 0 #open.
                elif(pins + self.Arr[self.frames][0][0] == 10):
                    self.Arr[self.frames][1] = 1 #spare.
                else:
                    raise Custom_Exception('A frame can not be more than 10.')
                self.frames += 1 
            elif(pins == 10):
                    self.Arr[self.frames][1] = 2 #strike.
                    self.frames += 1
        

    def score(self):
        if(self.frames != 10):
            raise Custom_Exception('Invalid args')
        ans = 0
        for i in range(9):
            if(self.Arr[i][1] == 0):
                ans += sum(self.Arr[i][0])
            elif(self.Arr[i][1] == 1):
                ans += 10 + self.Arr[i+1][0][0]
            else:
                ans += 10
                if(i < 8):
                    if(self.Arr[i+1][1] == 2):
                        ans += 10 + self.Arr[i+2][0][0]
                    else:
                        ans += sum(self.Arr[i+1][0])
                else:
                    ans += self.Arr[i+1][0][0] + self.Arr[i+1][0][1]
        ans += sum(self.Arr[9][0])
        return ans
                

