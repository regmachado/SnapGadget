import unsio.input as uns_in
import unsio.output as uns_out
from sys import argv

'''
snapcopy.py

Copy a snapshot.

Any combination of the components (gas, halo, disk, bulge, stars) may be present.

Usage:

python3 snapcopy.py input output

'''

snapshotIn  = argv[1]
snapshotOut = argv[2]

#=============================================
#Read

s = uns_in.CUNS_IN(snapshotIn,'all')
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
# Write

sout = uns_out.CUNS_OUT(snapshotOut, 'gadget2')

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
