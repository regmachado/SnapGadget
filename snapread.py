import numpy as np
import unsio.input as uns_in

snapshot = 'snapshot_0000'

s = uns_in.CUNS_IN(snapshot,'all')
s.nextFrame()

_, time = s.getData('time')
_, mass = s.getData('halo','mass')
_, pos  = s.getData('halo','pos')
_, vel  = s.getData('halo','vel')

x = pos[0::3]
y = pos[1::3]
z = pos[2::3]
