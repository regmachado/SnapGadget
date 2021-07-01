import unsio.input as uns_in
import unsio.output as uns_out
import unsiotools.simulations.cfalcon as falcon
from sys import argv
import numpy as np

'''
snapcod.py

Shift snapshot to COD.

The point of highest density is computed using the
desired component: all, gas, halo, disk, bulge, stars.

Usage:

python3 snapcod.py input output all

'''

snapshotIn  = argv[1]
snapshotOut = argv[2]
using       = argv[3]

#=============================================
#Read

s = uns_in.CUNS_IN(snapshotIn, 'all', float32=True)
s.nextFrame()

PartType = ['ngas', 'nhalo', 'ndisk', 'nbulge', 'nstars']
Npart    = [0, 0, 0, 0, 0]

for (i, parttype) in enumerate(PartType):
    ok, nread = s.getData(parttype)
    if ok==1:
        Npart[i] = nread

Ngas   = Npart[0]
Nhalo  = Npart[1]
Ndisk  = Npart[2]
Nbulge = Npart[3]
Nstars = Npart[4]

if Ngas>0:
    _, mass0 = s.getData('gas', 'mass')
    _, pos0  = s.getData('gas', 'pos' )
    _, vel0  = s.getData('gas', 'vel' )
    _, rho0  = s.getData('gas', 'rho' )
    _, u0    = s.getData('gas', 'u'   )
    _, hsml0 = s.getData('gas', 'hsml')
else:
    mass0 = np.array([]).astype('float32')
    pos0  = np.array([]).astype('float32')
    vel0  = np.array([]).astype('float32')
    rho0  = np.array([]).astype('float32')
    u0    = np.array([]).astype('float32')
    hsml0 = np.array([]).astype('float32')

if Nhalo>0:
    _, mass1 = s.getData('halo', 'mass')
    _, pos1  = s.getData('halo', 'pos' )
    _, vel1  = s.getData('halo', 'vel' )
else:
    mass1 = np.array([]).astype('float32')
    pos1  = np.array([]).astype('float32')
    vel1  = np.array([]).astype('float32')

if Ndisk>0:
    _, mass2 = s.getData('disk', 'mass')
    _, pos2  = s.getData('disk', 'pos' )
    _, vel2  = s.getData('disk', 'vel' )
else:
    mass2 = np.array([]).astype('float32')
    pos2  = np.array([]).astype('float32')
    vel2  = np.array([]).astype('float32')    
   
if Nbulge>0:
    _, mass3 = s.getData('bulge', 'mass')
    _, pos3  = s.getData('bulge', 'pos' )
    _, vel3  = s.getData('bulge', 'vel' )
else:
    mass3 = np.array([]).astype('float32')
    pos3  = np.array([]).astype('float32')
    vel3  = np.array([]).astype('float32')

if Nstars>0:
    _, mass4 = s.getData('stars', 'mass')
    _, pos4  = s.getData('stars', 'pos' )
    _, vel4  = s.getData('stars', 'vel' )
else:
    mass4 = np.array([]).astype('float32')
    pos4  = np.array([]).astype('float32')
    vel4  = np.array([]).astype('float32')

_, time   = s.getData('time')

#=============================================
#Compute COD using the selected component

if (using=='all'):
    M = np.concatenate([mass0, mass1, mass2, mass3, mass4])
    P = np.concatenate([pos0 , pos1 , pos2 , pos3, pos4  ])
    V = np.concatenate([vel0 , vel1 , vel2 , vel3, vel4  ])

if (using=='gas'):
    M = mass0
    P = pos0
    V = vel0

if (using=='halo'):
    M = mass1
    P = pos1
    V = vel1
    
if (using=='disk'):
    M = mass2
    P = pos2
    V = vel2
    
if (using=='bulge'):
    M = mass3
    P = pos3
    V = vel3
    
if (using=='stars'):
    M = mass4
    P = pos4
    V = vel4

# compute density with falcon
cf = falcon.CFalcon()
_, DENS, _ = cf.getDensity(P, M)

COD = np.argwhere( DENS == np.max(DENS) ).flatten()

X  = P[0::3]
Y  = P[1::3] 
Z  = P[2::3]

VX = V[0::3]
VY = V[1::3] 
VZ = V[2::3]

XCOD  =  X[COD]
YCOD  =  Y[COD]
ZCOD  =  Z[COD]

VXCOD = VX[COD]
VYCOD = VY[COD]
VZCOD = VZ[COD]

# Shift all particles to COM

if Ngas>0:
    pos0[0::3]  = pos0[0::3] -  XCOD
    pos0[1::3]  = pos0[1::3] -  YCOD 
    pos0[2::3]  = pos0[2::3] -  ZCOD
    vel0[0::3]  = vel0[0::3] - VXCOD
    vel0[1::3]  = vel0[1::3] - VYCOD
    vel0[2::3]  = vel0[2::3] - VZCOD

if Nhalo>0:
    pos1[0::3]  = pos1[0::3] -  XCOD
    pos1[1::3]  = pos1[1::3] -  YCOD 
    pos1[2::3]  = pos1[2::3] -  ZCOD
    vel1[0::3]  = vel1[0::3] - VXCOD
    vel1[1::3]  = vel1[1::3] - VYCOD
    vel1[2::3]  = vel1[2::3] - VZCOD

if Ndisk>0:
    pos2[0::3]  = pos2[0::3] -  XCOD
    pos2[1::3]  = pos2[1::3] -  YCOD 
    pos2[2::3]  = pos2[2::3] -  ZCOD
    vel2[0::3]  = vel2[0::3] - VXCOD
    vel2[1::3]  = vel2[1::3] - VYCOD
    vel2[2::3]  = vel2[2::3] - VZCOD

if Nbulge>0:
    pos3[0::3]  = pos3[0::3] -  XCOD
    pos3[1::3]  = pos3[1::3] -  YCOD 
    pos3[2::3]  = pos3[2::3] -  ZCOD
    vel3[0::3]  = vel3[0::3] - VXCOD
    vel3[1::3]  = vel3[1::3] - VYCOD
    vel3[2::3]  = vel3[2::3] - VZCOD
    
if Nstars>0:
    pos4[0::3]  = pos4[0::3] -  XCOD
    pos4[1::3]  = pos4[1::3] -  YCOD 
    pos4[2::3]  = pos4[2::3] -  ZCOD
    vel4[0::3]  = vel4[0::3] - VXCOD
    vel4[1::3]  = vel4[1::3] - VYCOD
    vel4[2::3]  = vel4[2::3] - VZCOD

print( 'XCOD, YCOD, ZCOD = %f, %f, %f ' % (XCOD, YCOD, ZCOD) )

#=============================================
# Write

sout = uns_out.CUNS_OUT(snapshotOut, 'gadget2', float32=True)

if Ngas>0:
    sout.setData(mass0, 'gas', 'mass')
    sout.setData(pos0 , 'gas', 'pos' )
    sout.setData(vel0 , 'gas', 'vel' )
    sout.setData(rho0 , 'gas', 'rho' )
    sout.setData(u0   , 'gas', 'u'   )
    sout.setData(hsml0, 'gas', 'hsml')
    
if Nhalo>0:
    sout.setData(mass1, 'halo', 'mass')
    sout.setData(pos1 , 'halo', 'pos' )
    sout.setData(vel1 , 'halo', 'vel' )

if Ndisk>0:
    sout.setData(mass2, 'disk', 'mass')
    sout.setData(pos2 , 'disk', 'pos' )
    sout.setData(vel2 , 'disk', 'vel' )

if Nbulge>0:
    sout.setData(mass3, 'bulge', 'mass')
    sout.setData(pos3 , 'bulge', 'pos' )
    sout.setData(vel3 , 'bulge', 'vel' )

if Nstars>0:
    sout.setData(mass4, 'stars', 'mass')
    sout.setData(pos4 , 'stars', 'pos' )
    sout.setData(vel4 , 'stars', 'vel' )

sout.setData(time, 'time')

sout.save()
sout.close()
