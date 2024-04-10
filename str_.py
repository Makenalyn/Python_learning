#!/usr/bin/python3

class strrep:
    def __init__(self, str1, str2, str3):
        self.str1 = str1
        self.str2 = str2
        self.str3 = str3

    def __repr__(self):
        return("{}, {}, {}".format(self.str1, self.str2, self.str3))

