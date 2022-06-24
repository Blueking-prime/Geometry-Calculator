class Point:
    def __init__(self, points):
        self.n = points
        self.points = []
        for p in range(points):
            self.points.append(0)

    def input_points(self):
        print ('Enter co-ordinates in order x-y-z, starting with the first point.')
        for p in range(self.n):
            self.points[p] = float(input('Co-ordinate '+str(p+1)+' : '))

    def measuredist(self):
        if self.n == 3:
            x, y, z, = self.points
            return (x**2 + y**2 + z**2)**0.5
        elif self.n == 6:
            x, y, z, x1, y1, z1 = self.points
            return ((x1-x)**2 + (y1-y)**2 + (z1-z)**2)**0.5
        elif self.n == 9:
            print ('This involves arcs and shit, and I\'m not gonna deal wth that just yet')

    def measurearea(self):
        if self.n == 3:
            x, y, z, = self.points
            if x == 0 or y == 0 or z == 0:
                if x == 0:
                    return y*z
                elif y == 0:
                    return x*z
                else:
                    return x*y
            else:
                print ('Between:') 
                print ('1) x and y')
                print ('2) x and z')
                print ('3) y and z')
                term = input('What side are we talking about? ')
                if term == '1' or term == 'x and y':
                    return x * y
                elif term == '2' or term == 'x and z':
                    return x * z
                elif term == '3' or term == 'y and z':
                    return y * z
                else:
                    return 'Error!! Unrecognized side'
        elif self.n == 6:
            print ('I\'m just showing the side formed between the two points and the origin')
            print ('I may do what I did with 1 point for this')
            x, y, z, x1, y1, z1 = self.points
            a = (x**2 + y**2 + z**2)**0.5
            b = (x1**2 + y1**2 + z1**2)**0.5
            c = ((x1-x)**2 + (y1-y)**2 + (z1-z)**2)**0.5
            s = (a + b + c)*0.5
            return (s*(s-a)*(s-b)*(s-c))**0.5
        elif self.n == 9:
            x, y, z, x1, y1, z1, x2, y2, z2 = self.points
            print ('Do you mean the Area formed by the points')
            print ('1) INCLUDING the origin')
            print ('2) EXCLUDING the origin')
            ara = input('Which one? ')
            if ara == '1' or ara == 'INCLUDING' or ara == 'including' or ara == 'Including':
                print ('Between:') 
                print ('1) P1, P2 and The Origin')
                print ('2) P1, P3 and The Origin')
                print ('3) P2, P3 and The Origin')
                term = input('What face are we talking about? ')
                if term == '1' or term == 'P1, P2 and The Origin':
                    a = (x**2 + y**2 + z**2)**0.5
                    b = (x1**2 + y1**2 + z1**2)**0.5
                    c = ((x1-x)**2 + (y1-y)**2 + (z1-z)**2)**0.5
                    s = (a + b + c)*0.5
                    m = (s*(s-a)*(s-b)*(s-c))**0.5
                    return m
                elif term == '2' or term == 'P1, P3 and The Origin':
                    a = (x**2 + y**2 + z**2)**0.5
                    b = (x2**2 + y2**2 + z2**2)**0.5
                    c = ((x2-x)**2 + (y2-y)**2 + (z2-z)**2)**0.5
                    s = (a + b + c)*0.5
                    m = (s*(s-a)*(s-b)*(s-c))**0.5
                    return m
                elif term == '3' or term == 'P2, P3 and The Origin':
                    a = (x2**2 + y2**2 + z2**2)**0.5
                    b = (x1**2 + y1**2 + z1**2)**0.5
                    c = ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**0.5
                    s = (a + b + c)*0.5
                    m = (s*(s-a)*(s-b)*(s-c))**0.5
                    return m
                else:
                    return 'Error!! Unrecognized side'              
            elif ara == '2' or ara == 'EXCLUDING' or ara == 'excluding' or ara == 'Excluding':
                a = ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5
                b = ((x2-x)**2 + (y2-y)**2 + (z2-z)**2)**0.5
                c = ((x1-x)**2 + (y1-y)**2 + (z1-z)**2)**0.5
                s = (a + b + c)*0.5
                return (s*(s-a)*(s-b)*(s-c))**0.5
            else:
                return 'Unavailable'
                print ('Wrong input')

    def measurevol(self):
        if self.n == 3:
            x, y, z, = self.points
            return x*y*z
        elif self.n == 6:
            return 'uncalculabe because, duh!'
        elif self.n == 9:
            x, y, z, x1, y1, z1, x2, y2, z2 = self.points
            d_p = (x1-x)*(x2-x) + (y1-y)*(y2-y) + (z1-z)*(z2-z)
            mAB = ((x1-x)**2 + (y1-y)**2 + (z1-z)**2)**0.5
            mAC = ((x2-x)**2 + (y2-y)**2 + (z2-z)**2)**0.5

            check = d_p/(mAB * mAC)

            c_pk = x*y1 - y*x1
            c_pj = x*z1 - z*x1
            c_pi = y*z1 - z*y1

            g = c_pi
            h = c_pj
            i = c_pk

            k = g*x  + h*y  + i*z
            f = g*x2 + h*y2 + i*z2

            if check == 1.0 or check == 0.9999999999999999 or check == 1.0000000000000002:
                print ('Points lie in a straight line, they have no volume')
            elif f == k:
                print ('Points lie in same plane, No Volume')
            else:
                ck = (x-x2)*(y1-y2) - (y-y2)*(x1-x2)
                cj = (x-x2)*(z1-z2) - (z-z2)*(x1-x2)
                ci = (y-y2)*(z1-z2) - (z-z2)*(y1-y2)
                g1 = ci
                h1 = cj
                i1 = ck
                k1 = g1*x  + h1*y  + i1*z
                dist = abs(g1*0 + h1*0 + i1*0 + k1)
                dist2 = (g1**2 + h1**2 + i1**2)**0.5
                H = dist/dist2

                a = ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5
                b = ((x2-x)**2 + (y2-y)**2 + (z2-z)**2)**0.5
                c = ((x1-x)**2 + (y1-y)**2 + (z1-z)**2)**0.5
                s = (a + b + c)*0.5
                B = (s*(s-a)*(s-b)*(s-c))**0.5

                return (1/3)*B*H



    def slope(self):
        if self.n == 3:
            x, y, z, = self.points
            if x == 0 or y == 0 or z == 0:
                if x == 0:
                    return z/y
                elif y == 0:
                    return z/x
                else:
                    return y/x
            else:
                print ('1) x-y axis')
                print ('2) x-z axis')
                print ('3) y-z axis')
                print ('4) xyz axis')
                print ('which axis?')
                side = input('Slope on which side? ')
                if side == '1' or side == 'x-y':
                    return y/x
                elif side == '2' or side == 'x-z':
                    return z/x
                elif side == '3' or side == 'y-z':
                    return z/y
                elif side == '4' or side == 'xyz':
                    run = (y**2 + x**2)**0.5
                    rise = z
                    return rise/run
                else:
                    return 'Error!! Unrecognized axis'
        elif self.n == 6:
            x, y, z, x1, y1, z1 = self.points
            if x == x1:
                return 'Nonexistent'
            else:
                if z1 == 0 and z == 0:
                    return (y1-y)/(x1-x)
                else:
                    run = ((y1-y)**2 + (x1-x)**2)**0.5
                    rise = z1 - z
                    return rise/run
        elif self.n == 9:
            x, y, z, x1, y1, z1, x2, y2, z2 = self.points
            d_p = (x1-x)*(x2-x) + (y1-y)*(y2-y) + (z1-z)*(z2-z)
            mAB = ((x1-x)**2 + (y1-y)**2 + (z1-z)**2)**0.5
            mAC = ((x2-x)**2 + (y2-y)**2 + (z2-z)**2)**0.5

            check = d_p/(mAB * mAC)
            if check == 1.0 or check == 0.9999999999999999 or check == 1.0000000000000002:
                run = ((y1-y)**2 + (x1-x)**2)**0.5
                rise = z1 - z
                return rise/run
            else:
                return 'Points not in straight line, no slope exists'
        else:
            return 'Unavailable'


def longform():
    print ('''How many points are we dealing with? I can only handle two at the moment
    - 1
    - 2
    - 3''')
    no_of_points = int(input('Points: '))
    if no_of_points > 3:
        print ('You no dey read abi?')
    else:
        no_points = no_of_points*3
        graph = Point(no_points) 
    print ('')
    print ('Okay, let\'s get the co-ordinates')
    graph.input_points()
    print ('')
    print ('''So now, what do you want me to do?
    Currently I can find:''')
    list_of_calculable_functions = ['-Distance', '-Area', '-Volume', '-Slope']
    for i in list_of_calculable_functions:
        print (i)
    print ('Please note that if only one point is supplied, all calculations will be done relative to the origin!')
    print ('')
    func = (input('So, which fuction? '))
    print ('')
    if func == 'Area':
        print ('The Area is', graph.measurearea())
    elif func == 'area':
        print ('The Area is', graph.measurearea())
    elif func == 'Volume':
        print ('The Volume is', graph.measurevol())
    elif func == 'volume':
        print ('The Volume is', graph.measurevol())
    elif func == 'Distance':
        print ('The Distance is', graph.measuredist())
    elif func == 'Distance':
        print ('The Distance is', graph.measuredist())
    elif func == 'Slope':
        print ('The Slope is', graph.slope())
    elif func == 'slope':
        print ('The Slope is', graph.slope())
    else:
        print ('I can\'t perform that function yet, Sorry')

def shortform():
    no_of_points = int(input('No of Points: '))
    no_points = no_of_points*3
    graph = Point(no_points)
    print ('')
    graph.input_points()
    print ('')
    func = (input('Which fuction? '))
    print ('')
    if func == 'Area':
        print ('The Area is', graph.measurearea())
    elif func == 'area':
        print ('The Area is', graph.measurearea())
    elif func == 'Volume':
        print ('The Volume is', graph.measurevol())
    elif func == 'volume':
        print ('The Volume is', graph.measurevol())
    elif func == 'Distance':
        print ('The Distance is', graph.measuredist())
    elif func == 'Distance':
        print ('The Distance is', graph.measuredist())
    elif func == 'Slope':
        print ('The Slope is', graph.slope())
    elif func == 'slope':
        print ('The Slope is', graph.slope())
    else:
        print ('I can\'t perform that function yet, Sorry')


#Okay, time for body code (Should probably change this to expansion code)
#Imagine if someone looked at this block and thought that was all there was to this code
print ('''This is a program to calculate stuff in a 3D plane.
Let\'s begin!

(Btw this program isn\'t caps sensitive)
''')
form = input('''Are you in a rush or do you have time?
-Rush (or any other input)
-Take your time
- ''' )
if form == 'Take your time' or form == 'take your time':
    longform()
else:
    shortform()