from z3 import *

l = "13,x,x,41,x,x,x,x,x,x,x,x,x,641,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,661,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23"
l = l.replace('x','1')
l = [ int(x) for x in l.split(',') ]

g = []
for idx,val in enumerate(l):
    if val != 1:
        g.append( [val,idx] )

g = sorted( g, key=lambda x: x[0], reverse=True)

# [[661, 44], [641, 13], [41, 3], [37, 50], [29, 42], [23, 67], [19, 25], [17, 30], [13, 0]]

print(g)
s = Solver()
last=0
x = Int('x')
y = Int('y')
z = Int('z')
v = Int('v')
e = Int('e')

C = Int('c')

s = Solver()

s.add( x > 302571860816)
s.add( y >  15384615384615 )
s.add( z > 4878048780487 )
s.add( v > 312012480499)
s.add( C > 200000000000000)
s.add( e > 10000000)

s.add( (13*y) == C )
s.add( (661*x)-44 == C )
s.add( (41*z)-3 == C )
s.add( (641*v)-13 == C)
s.add( (23*e)-67 == C)

while s.check() == sat :
    
    # find a possible solution
    ret = s.model()
    print("try this:", ret[C])
    s.add( x != ret[x])

    # try the solution
    c = ret[C].as_long() 
    
    if all( [ (c + idx) % val == 0 for idx,val in enumerate(l) ] ):
        print("Found it at:", c)
        break
