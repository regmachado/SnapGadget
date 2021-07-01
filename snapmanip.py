import unsio.input as uns_in
import unsio.output as uns_out
from sys import argv
import numpy as np

'''
snapmanip.py

Empty example of how to manipulate the disk positions and reshape the array before saving the new snapshot.

Usage:

python3 snapmanip.py input output

'''

snapshotIn  = argv[1]
snapshotOut = argv[2]

#==============================================
# Read
s = uns_in.CUNS_IN(snapshotIn,'all')
s.nextFrame()

_, time   = s.getData('time')

_, mdisk   = s.getData('disk','mass')
_, posdisk = s.getData('disk','pos')
_, veldisk = s.getData('disk','vel')

_, mhalo   = s.getData('halo','mass')
_, poshalo = s.getData('halo','pos')
_, velhalo = s.getData('halo','vel')

#==============================================
# Manipulate the disk positions:

x = posdisk[0::3]
y = posdisk[1::3]
z = posdisk[2::3]

#do something
#x = x....
#y = y....
#z = z....














#newpos  : a 2D array of shape (3,Ndisk)
newpos  = np.array( [x, y, z] )

#posdisk : a 1D array of length 3*Ndisk
posdisk = newpos.T.astype('float32').flatten()

#==============================================
# Write
sout = uns_out.CUNS_OUT(snapshotOut,'gadget2')

sout.setData(time,'time')

sout.setData(mhalo,'halo','mass')
sout.setData(mdisk,'disk','mass')

sout.setData(poshalo,'halo','pos')
sout.setData(posdisk,'disk','pos')

sout.setData(velhalo,'halo','vel')
sout.setData(veldisk,'disk','vel')

sout.save()
sout.close()
