#Moirepattern

Moirepattern is a python library that allows the user to construct moire patterns on the fly.
CURRENTLY JUST SUPPORTING SIMPLE MOIRE PATTERNS CREATING, THATS MEAN, YOU CAN ONLY USE IT FOR MAKING INTERFECENCE PATTERNS CONTROLLING THE ANGLE AND DISTANCE BETWEEN INTERFERENCES

Currently, to use it, please use:

pip install git+https://github.com/funkaro1/moire-constructor.git

then you can import Moirepattern using:

import Moirepattern

Next, you can create a moire object using Moire(interference_distance, base_grid_gap, angle)

Where interference distance is the distance between 2 interference lines (in 3d cases, this represent the distance of the interferences on the surface, without distortion), base_grid_gap correspond to the gap between the lines that conforms the base grid (that is, the equidistant grid that is superimposted to create the desired moiré pattern, and angle is the angle of the interference lines.

After creating a moiré object, size must be defined using set_size(x_size, y_size)

Finally, the moiré pattern must be created using make(Moire_type), where Moire_type is an sting containing the type of interference that would be created. Currently, just "simple" interference can be used.

For exporting the result, you can use export(filename) and export_base(filename)

Also, the lines can be accessed using .poly on the moiré object. It returns an array with arrays containing the points that conforms a line.
