# PyTangtv

PyTangtv is a set of tools used to work with data from LLNL Tangential viewing camera diagnostics from the DIII-D experiment.

Picker - program to select features from the loaded image and output the pixel coordinates. If a calibration board module is provided then the program can output x,y,z coordinates as well.

Pymask - program to generate an image mask by freehand drawing over an image. Drawing is kept in a seperate layer and then written out as a tiff on exit. This is used by our tomographic reconstruction code to indicate regions of the camera image that are to be excluded from the fit. Used to exclude things such as reflections or other artifacts from the fit.

PyAlign - program to do simple, rigid, image plane transformations of the loaded image. A background image can be loaded and then the two layered to facilitate aligning the two.

PyMorph - used to determine the foreground->background control points to do polynomial spatial warping of the foreground to match the background. Used to fix spherical aberations in an image.

