import moireclass as mc

# Create a new Moire object
moire_test = mc.Moire(10,1,90)
moire_test.setsize(20,20)
moire_test.make("Simple")
for points in moire_test.points:
    print(points[0],points[1],points[2],points[3])
    