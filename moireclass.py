import simple

class Moire:
    def __init__(self,d,c,angle):
        self.d = d
        self.c = c
        self.angle = angle
        self.points = []
        self.type = ""
    
    def setsize(self, x , y):
        self.xsize = x
        self.ysize = y
        
        
    def make(self,type):
        self.type = type
        if self.type == "Simple":
            simple.makeSimpleMoire(self)
        else:
            print("Not implemented yet // Not a valid type")