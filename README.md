# stns
stns is a collection of various scripts used in the Nusbaum lab's python analysis.

How do I use stns?
-------------
stns is used primarily for spike detection and data visualizing, an example of loading the main GUI is shown below.
Various plotting functions can be found in the module plot.

```python
from stns import SpikeDetectionGUI

# Launch a spike detection gui
dir_name = '/Users/loganfickling/Downloads/Lingli_Data_Transferred/Data/05-22-07/'
f_name = 'b0p057-cond 2LPG killed-ions stim 3_6V 14hz-cogs off-LG PD LP_export.smr'
app = SpikeDetectionGUI(provided_path=dir_name + f_name) # Or don't pass a path and enter it manually
app.mainloop()

```
See the documentation for more examples, or in python call help(functionname) to pull up the docstrings of the relevant
function

stns is currently in development; some features have not yet been implemented and there may be bugs.
See 'Development status' below.

Requirements
------------
scipy

numpy

pandas

matplotlib

seaborn

pandastable

brian2

neo

mat73


Quick start
-----------

stns can be installed using pip:

    $ pip install stns

If you want to run the latest version of the code, you can install from git:

    $mkdir crabby
    $cd crabby
    $git clone https://github.com/LoganJF/stns.git .
    $python setup.py install


Development status
------------------
Beta testing currently 0.0.4

