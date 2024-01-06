import moireclass as mc

# Create a new Moire object
moire_test = mc.Moire(15,1,181)
moire_test.setsize(20,20)
moire_test.make("Simple")


moire_test.export("test.svg")