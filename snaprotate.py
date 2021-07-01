import unsio.input as uns_in
import unsio.output as uns_out
from sys import argv
import numpy as np

'''
snaprotate.py

Rotate a snapshot.

Any combination of the components (gas, halo, disk, bulge, stars) may be present.
The angles must be given in degrees.
The rotations are applied around the x,y,z axes, in this order.

Usage:

python3 snaprotate.py input output 0 0 0

'''

snapshotIn  = argv[1]
snapshotOut = argv[2]

xrot        = float( argv[3] )
yrot        = float( argv[4] )
zrot        = float( argv[5] )

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

if Nhalo>0:
   _, mass1 = s.getData('halo', 'mass')
   _, pos1  = s.getData('halo', 'pos' )
   _, vel1  = s.getData('halo', 'vel' )

if Ndisk>0:
   _, mass2 = s.getData('disk', 'mass')
   _, pos2  = s.getData('disk', 'pos' )
   _, vel2  = s.getData('disk', 'vel' )
   
if Nbulge>0:
   _, mass3 = s.getData('bulge', 'mass')
   _, pos3  = s.getData('bulge', 'pos' )
   _, vel3  = s.getData('bulge', 'vel' )

if Nstars>0:
   _, mass4 = s.getData('stars', 'mass')
   _, pos4  = s.getData('stars', 'pos' )
   _, vel4  = s.getData('stars', 'vel' )

_, time   = s.getData('time')

#=============================================
# Rotate

xrot = np.radians(xrot)
yrot = np.radians(yrot)
zrot = np.radians(zrot)

def Rotate(coord, angle, around):
    #coord : 2D array of shape (3,Nbody)
    C, S = np.cos(angle), np.sin(angle)
    if(around=='x'):
        Rot = np.array([ [ 1,  0,  0 ], \
                         [ 0,  C, -S ], \
                         [ 0,  S,  C ] ])
    if(around=='y'):
        Rot = np.array([ [ C,  0,  S ], \
                         [ 0,  1,  0 ], \
                         [-S,  0,  C ] ])
    if(around=='z'):
        Rot = np.array([ [ C, -S,  0 ], \
                         [ S,  C,  0 ], \
                         [ 0,  0,  1 ] ])
    coordrot = np.dot(Rot, coord)
    return coordrot

def ApplyRotations(coord_):
    #coord_ : 1D array of length 3*Nbody
    #coord  : 2D array of shape (3,Nbody)
    coord = np.array( [ coord_[0::3], coord_[1::3], coord_[2::3] ] )
    if (xrot!=0):
        coord = Rotate(coord, xrot, 'x')
    if (yrot!=0):
        coord = Rotate(coord, yrot, 'y')
    if (zrot!=0):
        coord = Rotate(coord, zrot, 'z')
    coord_ = coord.T.flatten().astype('float32')
    return coord_
     
if Ngas>0:
    pos0 = ApplyRotations(pos0)
    vel0 = ApplyRotations(vel0)

if Nhalo>0:
    pos1 = ApplyRotations(pos1)
    vel1 = ApplyRotations(vel1)

if Ndisk>0:
    pos2 = ApplyRotations(pos2)
    vel2 = ApplyRotations(vel2)

if Nbulge>0:
    pos3 = ApplyRotations(pos3)
    vel3 = ApplyRotations(vel3)

if Nstars>0:
    pos4 = ApplyRotations(pos4)
    vel4 = ApplyRotations(vel4)

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
