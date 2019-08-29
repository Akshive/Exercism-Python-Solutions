class Garden(object):
    def __init__(self, diagram=None, students=['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']):
        self.Mat = [[' ' for j in range(24)] for i in range(2)]
        i = 0
        j = 0
        for c in diagram:
            if(c == '\n'):
                i += 1
                j = 0
            else:
                self.Mat[i][j] = c
                j += 1
        students.sort()
        self.Student_Indices = dict()
        idx = 0
        for student in students:
            self.Student_Indices[student] = idx
            idx += 2
        
    def plants(self, student):
        idx = self.Student_Indices[student]
        ans = []
        for i in range(2):
            for j in range(idx, idx+2):
                if(self.Mat[i][j] == 'R'):
                    ans.append('Radishes')
                elif(self.Mat[i][j] == 'C'):
                    ans.append('Clover')
                elif(self.Mat[i][j] == 'V'):
                    ans.append('Violets')
                else:
                    ans.append('Grass')
        return ans
