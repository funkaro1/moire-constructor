import Moirepattern as mc
# Create a new Moire object


print("1")
moire_test = mc.Moire(100, 5, -20) #already fixed
moire_test3 = mc.Moire(100, 5, -20) #already fixed
print("2")
moire_test.setsize(1000,1000)
print("3")
moire_test2 = mc.Moire(100, 5, 20) #already fixed
moire_test2.setsize(1000,1000)
moire_test.make("Simple", extra = 1.2)
moire_test2.make("Simple")
moire_test.add(moire_test2)
moire_test3.setsize(1000,1000)
moire_test.add_compound(moire_test3)
moire_test4 = mc.Moire(100, 5, 20) #already fixed
moire_test4.setsize(1000,1000) 
moire_test4.make("Simple")
moire_test.add_compound(moire_test4)
moire_test5 = mc.Moire(100, 5, -20) #already fixed
moire_test5.setsize(1000,1000)
moire_test5.make("Simple")
moire_test.add_compound(moire_test5)

print("4")
moire_test.export("test2.svg")
print("5")
moire_test.base_make()
moire_test.view()