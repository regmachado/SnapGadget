import unsio.input as uns_in
import unsio.output as uns_out
from sys import argv
import numpy as np

'''
snapjoin.py

Join two snapshots.

Any combination of the components (gas, halo, disk, bulge, stars) may be present in either of the snapshots.
The relative distances are Dx,Dy,Dz.
The relative velocities are Dvx,Dvy,Dvz.
By default, the output is shifted to the COM.

Usage:

python3 snapjoin.py inputA inputB output 0 0 0  0 0 0

'''

snapshotA   = argv[1]
snapshotB   = argv[2]
snapshotOut = argv[3]

Dx          = float( argv[4] )
Dy          = float( argv[5] )
Dz          = float( argv[6] )

Dvx         = float( argv[7] )
Dvy         = float( argv[8] )
Dvz         = float( argv[9] )

COM = True

#=============================================
#Read snapshot A

sA = uns_in.CUNS_IN(snapshotA, 'all', float32=True)
sA.nextFrame()

PartType = ['ngas', 'nhalo', 'ndisk', 'nbulge', 'nstars']
Npart    = [0, 0, 0, 0, 0]

for (i, parttype) in enumerate(PartType):
    ok, nread = sA.getData(parttype)
    if ok==1:
        Npart[i] = nread

NgasA   = Npart[0]
NhaloA  = Npart[1]
NdiskA  = Npart[2]
NbulgeA = Npart[3]
NstarsA = Npart[4]

print('\nFirst snapshot: %s' % snapshotA)
print('Ngas   = %d ' %  NgasA   )
print('Nhalo  = %d ' %  NhaloA  )
print('Ndisk  = %d ' %  NdiskA  )
print('Nbulge = %d ' %  NbulgeA )
print('Nstars = %d ' %  NstarsA )

if NgasA>0:
   _, mass0A = sA.getData('gas', 'mass')
   _, pos0A  = sA.getData('gas', 'pos' )
   _, vel0A  = sA.getData('gas', 'vel' )
   _, rho0A  = sA.getData('gas', 'rho' )
   _, u0A    = sA.getData('gas', 'u'   )
   _, hsml0A = sA.getData('gas', 'hsml')
else:
    mass0A = np.array([]).astype('float32')
    pos0A  = np.array([]).astype('float32')
    vel0A  = np.array([]).astype('float32')
    rho0A  = np.array([]).astype('float32')
    u0A    = np.array([]).astype('float32')
    hsml0A = np.array([]).astype('float32')
    
if NhaloA>0:
   _, mass1A = sA.getData('halo', 'mass')
   _, pos1A  = sA.getData('halo', 'pos' )
   _, vel1A  = sA.getData('halo', 'vel' )
else:
    mass1A = np.array([]).astype('float32')
    pos1A  = np.array([]).astype('float32')
    vel1A  = np.array([]).astype('float32')

if NdiskA>0:
   _, mass2A = sA.getData('disk', 'mass')
   _, pos2A  = sA.getData('disk', 'pos' )
   _, vel2A  = sA.getData('disk', 'vel' )
else:
    mass2A = np.array([]).astype('float32')
    pos2A  = np.array([]).astype('float32')
    vel2A  = np.array([]).astype('float32')   
   
if NbulgeA>0:
   _, mass3A = sA.getData('bulge', 'mass')
   _, pos3A  = sA.getData('bulge', 'pos' )
   _, vel3A  = sA.getData('bulge', 'vel' )
else:
    mass3A = np.array([]).astype('float32')
    pos3A  = np.array([]).astype('float32')
    vel3A  = np.array([]).astype('float32')

if NstarsA>0:
   _, mass4A = sA.getData('stars', 'mass')
   _, pos4A  = sA.getData('stars', 'pos' )
   _, vel4A  = sA.getData('stars', 'vel' )
else:
    mass4A = np.array([]).astype('float32')
    pos4A  = np.array([]).astype('float32')
    vel4A  = np.array([]).astype('float32')

_, timeA   = sA.getData('time')

#=============================================
#Read snapshot B

sB = uns_in.CUNS_IN(snapshotB, 'all', float32=True)
sB.nextFrame()

PartType = ['ngas', 'nhalo', 'ndisk', 'nbulge', 'nstars']
Npart    = [0, 0, 0, 0, 0]

for (i, parttype) in enumerate(PartType):
    ok, nread = sB.getData(parttype)
    if ok==1:
        Npart[i] = nread

NgasB   = Npart[0]
NhaloB  = Npart[1]
NdiskB  = Npart[2]
NbulgeB = Npart[3]
NstarsB = Npart[4]

print('\nSecond snapshot: %s' % snapshotB)
print('Ngas   = %d ' %  NgasB   )
print('Nhalo  = %d ' %  NhaloB  )
print('Ndisk  = %d ' %  NdiskB  )
print('Nbulge = %d ' %  NbulgeB )
print('Nstars = %d ' %  NstarsB )

if NgasB>0:
   _, mass0B = sB.getData('gas', 'mass')
   _, pos0B  = sB.getData('gas', 'pos' )
   _, vel0B  = sB.getData('gas', 'vel' )
   _, rho0B  = sB.getData('gas', 'rho' )
   _, u0B    = sB.getData('gas', 'u'   )
   _, hsml0B = sB.getData('gas', 'hsml')
else:
    mass0B = np.array([]).astype('float32')
    pos0B  = np.array([]).astype('float32')
    vel0B  = np.array([]).astype('float32')
    rho0B  = np.array([]).astype('float32')
    u0B    = np.array([]).astype('float32')
    hsml0B = np.array([]).astype('float32')
    
if NhaloB>0:
   _, mass1B = sB.getData('halo', 'mass')
   _, pos1B  = sB.getData('halo', 'pos' )
   _, vel1B  = sB.getData('halo', 'vel' )
else:
    mass1B = np.array([]).astype('float32')
    pos1B  = np.array([]).astype('float32')
    vel1B  = np.array([]).astype('float32')

if NdiskB>0:
   _, mass2B = sB.getData('disk', 'mass')
   _, pos2B  = sB.getData('disk', 'pos' )
   _, vel2B  = sB.getData('disk', 'vel' )
else:
    mass2B = np.array([]).astype('float32')
    pos2B  = np.array([]).astype('float32')
    vel2B  = np.array([]).astype('float32')   
   
if NbulgeB>0:
   _, mass3B = sB.getData('bulge', 'mass')
   _, pos3B  = sB.getData('bulge', 'pos' )
   _, vel3B  = sB.getData('bulge', 'vel' )
else:
    mass3B = np.array([]).astype('float32')
    pos3B  = np.array([]).astype('float32')
    vel3B  = np.array([]).astype('float32')

if NstarsB>0:
   _, mass4B = sB.getData('stars', 'mass')
   _, pos4B  = sB.getData('stars', 'pos' )
   _, vel4B  = sB.getData('stars', 'vel' )
else:
    mass4B = np.array([]).astype('float32')
    pos4B  = np.array([]).astype('float32')
    vel4B  = np.array([]).astype('float32')

_, timeB   = sB.getData('time')

#=============================================
# Shift snapshot B

if NgasB>0:
   pos0B[0::3] = pos0B[0::3] + Dx
   pos0B[1::3] = pos0B[1::3] + Dy
   pos0B[2::3] = pos0B[2::3] + Dz
   vel0B[0::3] = vel0B[0::3] + Dvx
   vel0B[1::3] = vel0B[1::3] + Dvy
   vel0B[2::3] = vel0B[2::3] + Dvz   

if NhaloB>0:
   pos1B[0::3] = pos1B[0::3] + Dx
   pos1B[1::3] = pos1B[1::3] + Dy
   pos1B[2::3] = pos1B[2::3] + Dz
   vel1B[0::3] = vel1B[0::3] + Dvx
   vel1B[1::3] = vel1B[1::3] + Dvy
   vel1B[2::3] = vel1B[2::3] + Dvz

if NdiskB>0:
   pos2B[0::3] = pos2B[0::3] + Dx
   pos2B[1::3] = pos2B[1::3] + Dy
   pos2B[2::3] = pos2B[2::3] + Dz
   vel2B[0::3] = vel2B[0::3] + Dvx
   vel2B[1::3] = vel2B[1::3] + Dvy
   vel2B[2::3] = vel2B[2::3] + Dvz
   
if NbulgeB>0:
   pos3B[0::3] = pos3B[0::3] + Dx
   pos3B[1::3] = pos3B[1::3] + Dy
   pos3B[2::3] = pos3B[2::3] + Dz
   vel3B[0::3] = vel3B[0::3] + Dvx
   vel3B[1::3] = vel3B[1::3] + Dvy
   vel3B[2::3] = vel3B[2::3] + Dvz
   
if NstarsB>0:
   pos4B[0::3] = pos4B[0::3] + Dx
   pos4B[1::3] = pos4B[1::3] + Dy
   pos4B[2::3] = pos4B[2::3] + Dz
   vel4B[0::3] = vel4B[0::3] + Dvx
   vel4B[1::3] = vel4B[1::3] + Dvy
   vel4B[2::3] = vel4B[2::3] + Dvz

#=============================================
# Concatenate A and B

if ((NgasA>0) or (NgasB>0)):
    mass0 = np.concatenate([mass0A, mass0B])
    pos0  = np.concatenate([pos0A , pos0B] )
    vel0  = np.concatenate([vel0A , vel0B] )
    rho0  = np.concatenate([rho0A , rho0B] )
    u0    = np.concatenate([u0A   , u0B]   )
    hsml0 = np.concatenate([hsml0A, hsml0B])
else:
    mass0 = np.array([]).astype('float32')
    pos0  = np.array([]).astype('float32')
    vel0  = np.array([]).astype('float32')

if ((NhaloA>0) or (NhaloB>0)):
    mass1 = np.concatenate([mass1A, mass1B])
    pos1  = np.concatenate([pos1A , pos1B] )
    vel1  = np.concatenate([vel1A , vel1B] )
else:
    mass1 = np.array([]).astype('float32')
    pos1  = np.array([]).astype('float32')
    vel1  = np.array([]).astype('float32')

if ((NdiskA>0) or (NdiskB>0)):
    mass2 = np.concatenate([mass2A, mass2B])
    pos2  = np.concatenate([pos2A , pos2B] )
    vel2  = np.concatenate([vel2A , vel2B] )
else:
    mass2 = np.array([]).astype('float32')
    pos2  = np.array([]).astype('float32')
    vel2  = np.array([]).astype('float32')
    
if ((NbulgeA>0) or (NbulgeB>0)):
    mass3 = np.concatenate([mass3A, mass3B])
    pos3  = np.concatenate([pos3A , pos3B] )
    vel3  = np.concatenate([vel3A , vel3B] )
else:
    mass3 = np.array([]).astype('float32')
    pos3  = np.array([]).astype('float32')
    vel3  = np.array([]).astype('float32')
    
if ((NstarsA>0) or (NstarsB>0)):
    mass4 = np.concatenate([mass4A, mass4B])
    pos4  = np.concatenate([pos4A , pos4B] )
    vel4  = np.concatenate([vel4A , vel4B] )
else:
    mass4 = np.array([]).astype('float32')
    pos4  = np.array([]).astype('float32')
    vel4  = np.array([]).astype('float32')

#=============================================
# Compute COM using all particles

if COM==True:
    
    print('\nShifting to center or mass')
    
    massall = np.concatenate([mass0, mass1, mass2, mass3, mass4])
    posall  = np.concatenate([pos0 , pos1 , pos2 , pos3, pos4  ])
    velall  = np.concatenate([vel0 , vel1 , vel2 , vel3, vel4  ])

    MTOT  = np.sum(massall)
    XCOM  = np.sum(massall*posall[0::3]) / MTOT
    YCOM  = np.sum(massall*posall[1::3]) / MTOT
    ZCOM  = np.sum(massall*posall[2::3]) / MTOT
    VXCOM = np.sum(massall*velall[0::3]) / MTOT
    VYCOM = np.sum(massall*velall[1::3]) / MTOT
    VZCOM = np.sum(massall*velall[2::3]) / MTOT

# Shift all particles to COM

    if ((NgasA>0) or (NgasB>0)):
        pos0[0::3]  = pos0[0::3] -  XCOM
        pos0[1::3]  = pos0[1::3] -  YCOM 
        pos0[2::3]  = pos0[2::3] -  ZCOM
        vel0[0::3]  = vel0[0::3] - VXCOM
        vel0[1::3]  = vel0[1::3] - VYCOM
        vel0[2::3]  = vel0[2::3] - VZCOM

    if ((NhaloA>0) or (NhaloB>0)):
        pos1[0::3]  = pos1[0::3] -  XCOM
        pos1[1::3]  = pos1[1::3] -  YCOM 
        pos1[2::3]  = pos1[2::3] -  ZCOM
        vel1[0::3]  = vel1[0::3] - VXCOM
        vel1[1::3]  = vel1[1::3] - VYCOM
        vel1[2::3]  = vel1[2::3] - VZCOM

    if ((NdiskA>0) or (NdiskB>0)):
        pos2[0::3]  = pos2[0::3] -  XCOM
        pos2[1::3]  = pos2[1::3] -  YCOM 
        pos2[2::3]  = pos2[2::3] -  ZCOM
        vel2[0::3]  = vel2[0::3] - VXCOM
        vel2[1::3]  = vel2[1::3] - VYCOM
        vel2[2::3]  = vel2[2::3] - VZCOM

    if ((NbulgeA>0) or (NbulgeB>0)):
        pos3[0::3]  = pos3[0::3] -  XCOM
        pos3[1::3]  = pos3[1::3] -  YCOM 
        pos3[2::3]  = pos3[2::3] -  ZCOM
        vel3[0::3]  = vel3[0::3] - VXCOM
        vel3[1::3]  = vel3[1::3] - VYCOM
        vel3[2::3]  = vel3[2::3] - VZCOM
        
    if ((NstarsA>0) or (NstarsB>0)):
        pos4[0::3]  = pos4[0::3] -  XCOM
        pos4[1::3]  = pos4[1::3] -  YCOM 
        pos4[2::3]  = pos4[2::3] -  ZCOM
        vel4[0::3]  = vel4[0::3] - VXCOM
        vel4[1::3]  = vel4[1::3] - VYCOM
        vel4[2::3]  = vel4[2::3] - VZCOM

#=============================================
# Write

sout = uns_out.CUNS_OUT(snapshotOut, 'gadget2', float32=True)

if ((NgasA>0) or (NgasB>0)):
    sout.setData(mass0, 'gas', 'mass')
    sout.setData(pos0 , 'gas', 'pos' )
    sout.setData(vel0 , 'gas', 'vel' )
    sout.setData(rho0 , 'gas', 'rho' )
    sout.setData(u0   , 'gas', 'u'   )
    sout.setData(hsml0, 'gas', 'hsml')
    
if ((NhaloA>0) or (NhaloB>0)):
    sout.setData(mass1, 'halo', 'mass')
    sout.setData(pos1 , 'halo', 'pos' )
    sout.setData(vel1 , 'halo', 'vel' )

if ((NdiskA>0) or (NdiskB>0)):
    sout.setData(mass2, 'disk', 'mass')
    sout.setData(pos2 , 'disk', 'pos' )
    sout.setData(vel2 , 'disk', 'vel' )

if ((NbulgeA>0) or (NbulgeB>0)):
    sout.setData(mass3, 'bulge', 'mass')
    sout.setData(pos3 , 'bulge', 'pos' )
    sout.setData(vel3 , 'bulge', 'vel' )

if ((NstarsA>0) or (NstarsB>0)):
    sout.setData(mass4, 'stars', 'mass')
    sout.setData(pos4 , 'stars', 'pos' )
    sout.setData(vel4 , 'stars', 'vel' )

sout.setData(timeA, 'time')

sout.save()
sout.close()
