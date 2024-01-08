import Moirepattern as mc
# Create a new Moire object
print("1")
moire_test = mc.Moire(-80, 10, -270)
print("2")
moire_test.setsize(1000,1000)
print("3")
moire_test.make("Simple")
print("4")
moire_test.export("test2.svg")
print("5")
moire_test.base_make()
moire_test.view()