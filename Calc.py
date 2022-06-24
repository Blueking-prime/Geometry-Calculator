#Project plan
print ('''We shall begin testing my physics calculator
Follow the prompts along these steps
1. Input physical parameters #clear
2. Select Operation out of Operation List #clear
3. Run with just one command #clear''')
print ('')

#Value input
#Variables
print ('Input your values')
l = float(input('Length = '))
w = float(input('Width = '))
d = float(input('Depth/Height = '))
t = float(input('Time elapsed = '))
m = float(input('Mass = '))
#Constants
g = 9.8
c = 299792458
G = 6.67408*20**-11

print ('')
#Available Functions
def area(l,w):
    return l*w
def volume(l,w,d):
    return l*w*d
def density(l,w,d,m):
    return m/(l*w*d)
def velocity(l,t):
    return l/t
def weight(m, g):
    return m*g

#Select Function
list_of_calc_func = ['-Area', '-Volume', '-Density', '-Weight', '-\"More coming soon\"']
print ('This Program can calculate:')
for item in list_of_calc_func:
    print (item)
print ('')
func = input('So, what function are we running today? ')
print ('')
def func2run(func):
    if func == 'Area':
        print ('The Area is', area(l,w))
    elif func == 'area':
        print ('The Area is ', area(l,w))
    elif func == 'Volume':
        print ('The Volume is ', volume(l,w,d))
    elif func == 'volume':
        print ('The Volume is ', volume(l,w,d))
    elif func == 'Density':
        print ('The Density is ', density(l,w,d,m))
    elif func == 'density':
        print ('The Density is ', density(l,w,d,m))
    elif func == 'Velocity':
        print ('The Velocity is ', velocity(l,t))
    elif func == 'velocity':
        print ('The Velocity is ', velocity(l,t))
    elif func == 'speed':
        print ('The Speed is ', velocity(l,t))
    elif func == 'Speed':
        print ('The Speed is ', velocity(l,t))
    elif func == 'Weight':
        print ('The weight is ', weight(m,g))
    elif func == 'weight':
        print ('The weight is ', weight(m,g))
    else:
        if func == "More coming soon":
            print ('Screw You')
            print ('Abi you think say you dey wise')
        elif func == "more coming soon":
            print ('screw you')
            print ('abi you think say you dey wise')
        else:
            print ('I can\'t perform that function yet, Sorry')
func2run(func)