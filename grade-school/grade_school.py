import operator
class School(object):
    def __init__(self):
        self.Roster = dict()

    def add_student(self, name, grade):
        self.Roster[name] = grade

    def roster(self):
        sorted_roster = sorted(self.Roster.items(), key = lambda x : (x[1], x[0]))
        ans = []
        for (i, j) in sorted_roster:
            ans.append(i)
        return ans

    def grade(self, grade_number):
        ans = []
        for key, val in self.Roster.items():
            if(val == grade_number):ans.append(key)
        ans.sort()
        return ans
