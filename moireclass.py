import simple
import bool
import svgexport as svg

#Moire class
class Moire:
    def __init__(self,d,c,angle):
        self.d = d
        self.c = c
        self.angle = angle
        self.poly = []
        self.type = ""
        self.parts = 1
        self.structure = [1] #this will be a matrix with the shape of the structure; Zeroes in every pos unless is the corresponding part
        self.rows = 1
        self.cols = 1
    
    def setsize(self, x , y):
        self.xsize = x
        self.ysize = y
        
        
    def make(self,type):
        self.type = type
        if self.type == "Simple":
            simple.makeSimpleMoire(self)
        else:
            print("Not implemented yet // Not a valid type")
            
    def export(self,filename):
        to_export = []
        for i in range(self.parts):
            x_size = self.xsize/self.cols
            y_size = self.ysize/self.rows
            x_pos = (i%self.cols)*x_size
            #create a box with the size of the part
            box = [[-x_size/2,-y_size/2],[-x_size/2,y_size/2],[x_size/2,y_size/2],[x_size/2,-y_size/2]] #ill be adjusting the points positions when some part is added
            #iterate through the lines and check if they intersect with the box
            #if they do, add the intersection points to the list
            for line in self.poly:
                if bool.intersect(line,box)[0]:
                    to_export.append(bool.intersect(line,box))
            to_export = [sublist[0] for sublist in to_export]
            print(to_export)
            svg.export(to_export,x_size,y_size,filename)
                