#!/usr/bin/env python
"""
reading PFISR data down to IQ samples

See Examples/ for more updated specific code
"""
from isrutils import Path
from isrutils.common import boilerplateapi
from isrutils.looper import simpleloop
#%% user parameters
p = boilerplateapi()
P={
'path':p.isrfn,
'beamid': 64157,
'acf': True,
'vlimacf': (18,45),
'zlim_pl': p.zlim,
'vlim_pl': [72,90],
'flim_pl': [3.5,5.5],
'odir': p.odir,
'vlim': [25, 55],
'zlim': p.zlim,
'tlim': p.tlim,
'verbose': True,}
#%% read and plot
flist = [x for x in Path(P['path']).expanduser().iterdir() if x.suffix=='.h5']

simpleloop(flist,P)