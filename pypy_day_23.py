import IPython

class dllist():
    def __init__(self, init_list):
        self.data = {}
        a = init_list.pop(0)
        self.data[a] = [a,a]
        self.head = a
        
        prev = a
        for a in init_list:
            if a == self.head:
                continue
            self.data[a] = [prev, 0]
            self.data[prev][1] = a  # update the next for the last
            prev = a

        self.data[prev][1] = self.head  # point the tail to the head
        self.data[self.head][0] = prev  # point the head to the tail
    
    # insert v after n
    def insert_after(self,n, v):
        #print("insert {} after {}".format(v,n))
        n_next = self.data[n][1]
        self.data[n][1] = v
        self.data[n_next][0] = v
        self.data[v] = [n, n_next]
        
    def remove(self,v):
        prev = self.data[ v ][0] #prev
        next = self.data[ v ][1] #next

        if v == self.head:
            self.head = next

        self.data[prev][1] = next
        self.data[next][0] = prev
        
    def __str__(self):
        ret = []
        n = self.head
        ret += [ n ]
        while True:
            n = self.data[n][1]
            if n == self.head:
                break
            ret += [n]
        return "--".join([ str(x) for x in ret])
    
puz_input = "476138259"
#puz_input = "389125467"

print("Using puzzle input:", puz_input)
puz_input = [int(x) for x in list(puz_input)]

## part2
print("Loading Data")
maxn = max(puz_input)
print("starting adding from:", maxn)

while True:
    maxn +=1
    puz_input.append(maxn)
    if maxn == 1000000:
        break

print("len:", len(puz_input))

print("Creating LL")
dll = dllist([int(x) for x in list(puz_input)])

print("Starting Puzzle")
current=puz_input[0]
for i in range(0,10000000):
#for i in range(0,100):
    # get the next 3 cups
    v1 = dll.data[current][1]  # value after 3
    v2 = dll.data[v1][1] 
    v3 = dll.data[v2][1]

    removed = [v1,v2,v3]
    dll.remove(v1)
    dll.remove(v2)
    dll.remove(v3)

    dst = current - 1
    if dst == 0:
        # dst = 9
        dst = 1000000 
    while dst in removed:
        dst -= 1
        if dst < 1:
            # dst = 9
            dst =1000000 

    
    a = removed.pop(0)
    dll.insert_after(dst, a)
    b = removed.pop(0)
    dll.insert_after(a,b)
    c = removed.pop(0)
    dll.insert_after(b,c)

    #print(i+1, current, dst, dll)
    current = dll.data[current][1] # get the cup after the current

    if dll.data[1][1] == 934001:
        print("Found match at", i)

n=dll.data[1][1] # the number after 1

## Part 1 answer
"""
n=dll.data[1][1] # the number after 1
ret=""
while n != 1:
    ret += str(n)
    n = dll.data[n][1]
print(ret)
"""

## Part 2 answer
n=dll.data[1][1] # the number after 1
n2 = dll.data[n][1]
print( n)
print( n2)
print( n * n2)


#IPython.embed()
 

