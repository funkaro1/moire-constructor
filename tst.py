import moire
import vis

test = moire.Structure(0.5)
test2 = moire.Structure(0.5)
test.create(10, 41, 50, 50, "simple", 0)
test.extend(10, 10, "simple")
test.extend(65, 40, "simple")
test.view(2)
