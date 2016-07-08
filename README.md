# NuGridpy3
**tl;dr: don't use this, use the official version here --> https://github.com/NuGrid/NuGridPy**

This is a version of NuGridpy that works with Python 3.

Original source: http://nugridpy.phys.uvic.ca

I used 2to3 and then manually adjusted indentations and such until I could run `python setup.py install` with no errors under the new AstroConda Python 3.5. No promises, but it seems to work for me.

# Funny Story
It turns out I simply failed to find the up-to-date NuGridPy, which lives at https://github.com/NuGrid/NuGridPy! The version I found was linked from http://mesastar.org/tools-utilities/python-based-stuff/nugrids-mesa.py-1/nugrids-mesa.py, which led to https://pypi.python.org/pypi/NuGridpy, which, at the time of this writing hosts an old python-2-only version of NuGridPy.
