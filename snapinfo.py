import unsio.input as uns_in
import unsio.output as uns_out
from sys import argv

'''
snapinfo.py

Print information about a snapshot.

Usage:

python3 snapinfo.py input

'''

snapshot = argv[1]

#=============================================
#Read

s = uns_in.CUNS_IN(snapshot,'all')
s.nextFrame()

_, time  = s.getData('time')

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
NTOTAL = Ngas + Nhalo + Ndisk + Nbulge + Nstars

print('type   = %s' % s.getInterfaceType() )

print('time   = %f' % time )

print('Ngas   = %d ' % Ngas    )
print('Nhalo  = %d ' % Nhalo  )
print('Ndisk  = %d ' % Ndisk  )
print('Nbulge = %d ' % Nbulge )
print('Nstars = %d ' % Nstars )
print('NTOTAL = %d ' % NTOTAL )


Comp = ['gas', 'halo', 'disk', 'bulge', 'stars']

for i,comp in enumerate(Comp):
    
    if(Npart[i]>0):
        print('\n=================================')
        print(comp)
        print('=================================')

    okmass, mass = s.getData(comp, 'mass')
    okpos , pos  = s.getData(comp, 'pos' )
    okvel , vel  = s.getData(comp, 'vel' )
                             
    okrho , rho  = s.getData(comp, 'rho' )
    oku   , u    = s.getData(comp, 'u'   )
    okhsml, hsml = s.getData(comp, 'hsml')
    okids , ids  = s.getData(comp, 'id'  )
                             
    okpot , pot  = s.getData(comp, 'pot'  )
    okacc , acc  = s.getData(comp, 'acc'  )
    okage , age  = s.getData(comp, 'age'  )
    okmet , met  = s.getData(comp, 'metal')

    if okmass:
        print('\nmass =', mass)
    if okpos:
        print('\npos  =', pos)
    if okvel:
        print('\nvel  =', vel)
    if okrho:
        print('\nrho  =', rho)
    if oku:
        print('\nu    =', u)
    if okhsml:
        print('\nhsml =', hsml)
    if okids:
        print('\nids  =', ids)
    if okpot:
        print('\npot  =', pot)
    if okacc:
        print('\nacc  =', acc)
    if okage:
        print('\nage  =', age)
    if okmet:
        print('\nmetal=', met)

#=============================================

