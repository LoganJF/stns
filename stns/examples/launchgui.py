#!/usr/bin/env python
from stns.gui import SpikeDetectionGUI
from glob import glob
#file_name = '/Users/loganfickling/Downloads/Actinonin/data/11-1-20/11_1_20_LF_a.smr'
"""
file_name = '/Users/loganfickling/Downloads/most recent/1_28_21_LF_d.smr'
app = SpikeDetectionGUI(provided_path=file_name)
app.mainloop()"""

file_names = sorted(glob('/Users/loganfickling/Downloads/Hemo*/12-13*/*.smr'))
#file_names = sorted(glob('/Users/loganfickling/Desktop/Lingli- LPG kills and AB kills/11-03*/*.smr'))
#file_names = glob(file_name + 'Lingli_Data_Transferred/Data/*/*.smr')
for file_name in file_names:
    print('Starting file {}'.format(file_name),flush=True)
    app = SpikeDetectionGUI(provided_path=file_name)
    app.mainloop()
    del(app)

