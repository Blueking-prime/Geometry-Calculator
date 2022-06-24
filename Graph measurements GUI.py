from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.title('Graph Mesurements')
#root.geometry('325x180')
root.resizable(width=False, height=False)

l1 = []
true = 0
list_of_calculable_functions = ['-Distance', '-Area', '-Volume', '-Slope']

#this is just to remove underlining errors
graph = []
result = Entry(root)
long_win = []
r = 0
point_no = 0
class Point:
    def __init__(self, points):
        self.n = points
        self.points = []

    def input_points(self):
        self.points = []
        global l1
        for p in l1:
            self.points.append(p)
        l1 = []

    def measuredist(self):
        if self.n == 3:
            x, y, z, = self.points
            return (x**2 + y**2 + z**2)**0.5
        elif self.n == 6:
            x, y, z, x1, y1, z1 = self.points
            return ((x1-x)**2 + (y1-y)**2 + (z1-z)**2)**0.5
        elif self.n == 9:
            Label(long_win, text = 'This involves arcs and shit, and I\'m not gonna deal wth that just yet', font = ('Segoe UI Light', 11)).grid(row = r + 3, column = 1, columnspan = 4)

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
                Label(long_win, text = 'What side are we talking about?', font = ('Segoe UI Light', 11)).grid(row = r + 6, column = 0, columnspan = 2, pady = 5, padx = 10)
                def choice(term):
                    if term == 1:
                        res = x * y
                    elif term == 2:
                        res = x * z
                    elif term == 3:
                        res = y * z
                    result.delete(0, END)
                    result.insert(0, str(res))
                ttk.Button(long_win, text = 'x and y', command = lambda: choice(1)).grid(row = r + 7, column = 0, columnspan = 2, pady = 5, sticky = W+E, padx = (10, 9))
                ttk.Button(long_win, text = 'x and z', command = lambda: choice(2)).grid(row = r + 8, column = 0, columnspan = 2, pady = 5, sticky = W+E, padx = (10, 9))
                ttk.Button(long_win, text = 'y and z', command = lambda: choice(3)).grid(row = r + 9, column = 0, columnspan = 2, pady = 5, sticky = W+E, padx = (10, 9))
                
        elif self.n == 6:
            x, y, z, x1, y1, z1 = self.points
            a = (x**2 + y**2 + z**2)**0.5
            b = (x1**2 + y1**2 + z1**2)**0.5
            c = ((x1-x)**2 + (y1-y)**2 + (z1-z)**2)**0.5
            s = (a + b + c)*0.5
            return (s*(s-a)*(s-b)*(s-c))**0.5

        elif self.n == 9:
            #long_win.geometry('530x700')
            x, y, z, x1, y1, z1, x2, y2, z2 = self.points
            Label(long_win,
            text = 
            '''Do you mean the Area formed by the points
            - INCLUDING the origin
            - EXCLUDING the origin''', font = ('Segoe UI Light', 11)).grid(row = r + 3, column = 1, columnspan = 3, sticky = W, pady = 5)
            def choice_2(ara):
                if ara == 1:
                    Label(long_win, text = 'Between:', font = ('Segoe UI Light', 11)).grid(row = r + 5, column = 1, columnspan = 3, sticky = W, pady = 5)
                    def choice_in_choice_2(term):
                        if term == 1:
                            a = (x**2 + y**2 + z**2)**0.5
                            b = (x1**2 + y1**2 + z1**2)**0.5
                            c = ((x1-x)**2 + (y1-y)**2 + (z1-z)**2)**0.5
                            s = (a + b + c)*0.5
                            m = (s*(s-a)*(s-b)*(s-c))**0.5
                            res = m
                        elif term == 2:
                            a = (x**2 + y**2 + z**2)**0.5
                            b = (x2**2 + y2**2 + z2**2)**0.5
                            c = ((x2-x)**2 + (y2-y)**2 + (z2-z)**2)**0.5
                            s = (a + b + c)*0.5
                            m = (s*(s-a)*(s-b)*(s-c))**0.5
                            res = m
                        elif term == 3:
                            a = (x2**2 + y2**2 + z2**2)**0.5
                            b = (x1**2 + y1**2 + z1**2)**0.5
                            c = ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**0.5
                            s = (a + b + c)*0.5
                            m = (s*(s-a)*(s-b)*(s-c))**0.5
                            res = m
                        result.delete(0, END)
                        result.insert(0, str(res))
                    ttk.Button(long_win, text = 'P1, P2 and The Origin', command = lambda: choice_in_choice_2(1)).grid(row = r + 6, column = 1, pady = 5, sticky = W+E)
                    ttk.Button(long_win, text = 'P1, P3 and The Origin', command = lambda: choice_in_choice_2(2)).grid(row = r + 6, column = 3, pady = 5, sticky = W+E)
                    ttk.Button(long_win, text = 'P2, P3 and The Origin', command = lambda: choice_in_choice_2(3)).grid(row = r + 6, column = 5, pady = 5, sticky = W+E, padx = (0, 19))


                elif ara == 2:
                    a = ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5
                    b = ((x2-x)**2 + (y2-y)**2 + (z2-z)**2)**0.5
                    c = ((x1-x)**2 + (y1-y)**2 + (z1-z)**2)**0.5
                    s = (a + b + c)*0.5
                    res = (s*(s-a)*(s-b)*(s-c))**0.5
                    result.delete(0, END)
                    result.insert(0, str(res))
            ttk.Button(long_win, text = 'Including', command = lambda: choice_2(1)).grid(row = r + 4, column = 1, pady = 5, sticky = W+E)
            ttk.Button(long_win, text = 'Excluding', command = lambda: choice_2(2)).grid(row = r + 4, column = 5, pady = 5, padx = (0, 19), sticky = W+E)

    def measurevol(self):
        if self.n == 3:
            x, y, z, = self.points
            return x*y*z
        elif self.n == 6:
            return 'Uncalculable because, duh!'
        elif self.n == 9:
            #long_win.geometry('530x700')
            Label(long_win, text = '''Considering three points on a plane have no volume,
            I'm just gonna use the origin to make them 4''', font = ('Segoe UI Light', 11)).grid(row = r + 3, column = 1, columnspan = 4, pady = 5)
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
                Label(long_win, text = 'Points lie in a straight line, they have no volume', font = ('Segoe UI Light', 11)).grid(row = r + 4, column = 1, columnspan = 4)
            elif f == k:
                Label(long_win, text = 'Points lie in same plane, No Volume', font = ('Segoe UI Light', 11)).grid(row = r + 4, column = 2, columnspan = 4)
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
                Label(long_win, text = 'Slope on which axis?', font = ('Segoe UI Light', 11), anchor = W).grid(row = r + 6, column = 0, columnspan = 2, pady = 5, padx = 10, sticky = W + E)
                def choice_3(side):
                    if side == 1:
                        res = y/x
                    elif side == 2:
                        res = z/x
                    elif side == 3:
                        res = z/y
                    elif side == 4:
                        run = (y**2 + x**2)**0.5
                        rise = z
                        res = rise/run
                    result.delete(0, END)
                    result.insert(0, str(res))
                ttk.Button(long_win, text = 'x-y axis', command = lambda: choice_3(1)).grid(row = r + 7, column = 0, columnspan = 2, pady = 5, sticky = W+E, padx = (10, 9))
                ttk.Button(long_win, text = 'x-z axis', command = lambda: choice_3(2)).grid(row = r + 8, column = 0, columnspan = 2, pady = 5, sticky = W+E, padx = (10, 9))
                ttk.Button(long_win, text = 'y-z axis', command = lambda: choice_3(3)).grid(row = r + 9, column = 0, columnspan = 2, pady = 5, sticky = W+E, padx = (10, 9))
                ttk.Button(long_win, text = 'xyz axis', command = lambda: choice_3(4)).grid(row = r + 10, column = 0, columnspan = 2, pady = 5, sticky = W+E, padx = (10, 9))
                
        elif self.n == 6:
            x, y, z, x1, y1, z1 = self.points
            if x == x1:
                Label(long_win, text = 'Bros, Which maths wey you wan solve?\n You fit divide by 0?', font = ('Segoe UI Light', 11)).grid(row = r + 4, column = 1, columnspan = 3)
                return None
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
        
def longform():

    def measure(func):
        global result
        result = ttk.Entry(long_win)
        if point_no == 1:
            result.grid(row = 31, column = 0, columnspan = 2, sticky = W + E, pady = (0, 20), padx = 10)

            if func == 1:
                res = graph.measurearea()
                Label(long_win, text = 'The Area is ', font = ('Segoe UI Light', 11), anchor = W).grid(row = 30, column = 0, columnspan = 2, pady = 5, padx = 10, sticky = W + E)
                result.insert(0, str(res))
            elif func == 2:
                res = graph.measuredist()
                Label(long_win, text = 'The Distance is ', font = ('Segoe UI Light', 11), anchor = W).grid(row = 30, column = 0, columnspan = 2, pady = 5, padx = 10, sticky = W + E)
                result.insert(0, str(res))
            elif func == 3:
                res = graph.measurevol()
                Label(long_win, text = 'The Volume is ', font = ('Segoe UI Light', 11), anchor = W).grid(row = 30, column = 0, columnspan = 2, pady = 5, padx = 10, sticky = W + E)
                result.insert(0, str(res))
            elif func == 4:
                res = graph.slope()
                Label(long_win, text = 'The Slope is ', font = ('Segoe UI Light', 11), anchor = W).grid(row = 30, column = 0, columnspan = 2, pady = 5, padx = 10, sticky = W + E)
                result.insert(0, str(res))
        else:
            result.grid(row = 30, column = 2, columnspan = 4, sticky = W + E, pady = (10, 20), padx = (0, 20))

            if func == 1:
                res = graph.measurearea()
                Label(long_win, text = 'The Area is ', font = ('Segoe UI Light', 11), anchor = E).grid(row = 30, column = 1, pady = (10, 20), padx = 5, sticky = W + E)
                result.insert(0, str(res))
            elif func == 2:
                res = graph.measuredist()
                Label(long_win, text = 'The Distance is ', font = ('Segoe UI Light', 11), anchor = E).grid(row = 30, column = 1, pady = (10, 20), padx = 5, sticky = W + E)
                result.insert(0, str(res))
            elif func == 3:
                res = graph.measurevol()
                Label(long_win, text = 'The Volume is ', font = ('Segoe UI Light', 11), anchor = E).grid(row = 30, column = 1, pady = (10, 20), padx = 5, sticky = W + E)
                result.insert(0, str(res))
            elif func == 4:
                res = graph.slope()
                Label(long_win, text = 'The Slope is ', font = ('Segoe UI Light', 11), anchor = E).grid(row = 30, column = 1, pady = (10, 20), padx = 5, sticky = W + E)
                result.insert(0, str(res))
            

    def no_of_points(value):
        global point_no
        point_no = value
        global long_win
        long_win = Tk()
        long_win.title('Full Calc')
        if value == 1:
            long_win.title('Full Calc: 1-Point system')
            #long_win.geometry('220x200')
        elif value == 2:
            long_win.title('Full Calc: 2-Point System')
            #long_win.geometry('400x200')
        elif value == 3:
            long_win.title('Full Calc: 3-Point System')
            #long_win.geometry('530x200')
        long_win.resizable(width=False, height=False)

        no_points = value * 3
        global graph
        graph = Point(no_points)

        Label(long_win, text = 'First, the co-ordinates', font = ('Segoe UI Light', 11)).grid(row = 2, column = 0, columnspan = 2, padx = 10)

        def input_1():
            try:
                l1.append(float(p1x.get()))
                l1.append(float(p1y.get()))
                l1.append(float(p1z.get()))
                graph.input_points()
            except ValueError:
                messagebox.showerror('Invalid Values', 'There are some missing/incorrect values')
            else:
                Label(long_win, text = 'Currently I can find: ', justify = 'left', font = ('Segoe UI Light', 11)).grid(row = 9, column = 0, columnspan = 2, padx = 10, pady = 5, sticky = W)
                global r
                r = 10
                for index, i in enumerate(list_of_calculable_functions):
                    Label(long_win, text = i, font = ('Segoe UI Light', 11)).grid(row = index + 10, column = 0, columnspan = 2, padx = 10, sticky = W)
                    r += 1
                
                
                Label(long_win, text = 'So, which fuction?', font = ('Segoe UI Light', 11)).grid(row = r + 1, column = 0, columnspan = 2, padx = 10, pady = 5, sticky = W)

                ttk.Button(long_win, text = 'Area', command = lambda: measure(1)).grid(row = r + 4, column = 0, columnspan = 2, pady = 5, sticky = W+E, padx = (10, 9))
                ttk.Button(long_win, text = 'Volume', command = lambda: measure(3)).grid(row = r + 5, column = 0, columnspan = 2, pady = 5, sticky = W+E, padx = (10, 9))
                ttk.Button(long_win, text = 'Distance', command = lambda: measure(2)).grid(row = r + 2, column = 0, columnspan = 2, pady = 5, sticky = W+E, padx = (10, 9))
                ttk.Button(long_win, text = 'Slope', command = lambda: measure(4)).grid(row = r + 3, column = 0, columnspan = 2, pady = 5, sticky = W+E, padx = (10, 9))

        def input_2():
            try:
                l1.append(float(p1x.get()))
                l1.append(float(p1y.get()))
                l1.append(float(p1z.get()))
                l1.append(float(p2x.get()))
                l1.append(float(p2y.get()))
                l1.append(float(p2z.get()))
                graph.input_points()
            except ValueError:
                messagebox.showerror('Invalid Values', 'There are some missing/incorrect values')
            else:
                Label(long_win, text = '''So now, what do you want me to do?
                Currently I can find: ''', justify = 'left', font = ('Segoe UI Light', 11)).grid(row = 9, column = 1, columnspan = 3, pady = 5, sticky = W)
                global r
                r = 10
                for index, i in enumerate(list_of_calculable_functions):
                    Label(long_win, text = i, font = ('Segoe UI Light', 11)).grid(row = index + 10, column = 1, sticky = W)
                    r += 1
                
                
                Label(long_win, text = 'So, which fuction?', font = ('Segoe UI Light', 11)).grid(row = r + 1, column = 1, pady = 5, sticky = W)

                ttk.Button(long_win, text = 'Area', command = lambda: measure(1)).grid(row = r + 2, column = 3, pady = 5, sticky = W+E, padx = (0, 19))
                ttk.Button(long_win, text = 'Volume', command = lambda: measure(3)).grid(row = r + 3, column = 3, pady = 5, sticky = W+E, padx = (0, 19))
                ttk.Button(long_win, text = 'Distance', command = lambda: measure(2)).grid(row = r + 3, column = 1, pady = 5, sticky = W+E)
                ttk.Button(long_win, text = 'Slope', command = lambda: measure(4)).grid(row = r + 2, column = 1, pady = 5, sticky = W+E)

        def input_3():
            try:
                l1.append(float(p1x.get()))
                l1.append(float(p1y.get()))
                l1.append(float(p1z.get()))
                l1.append(float(p2x.get()))
                l1.append(float(p2y.get()))
                l1.append(float(p2z.get()))
                l1.append(float(p3x.get()))
                l1.append(float(p3y.get()))
                l1.append(float(p3z.get()))
                graph.input_points()
            except ValueError:
                messagebox.showerror('Invalid Values', 'There are some missing/incorrect values')
            else:
                Label(long_win, text = '''So now, what do you want me to do?
                Currently I can find: ''', justify = 'left', font = ('Segoe UI Light', 11)).grid(row = 9, column = 1, columnspan = 3, pady = 5, sticky = W)
                global r
                r = 10
                for index, i in enumerate(list_of_calculable_functions):
                    if index != 3:
                        Label(long_win, text = i, font = ('Segoe UI Light', 11)).grid(row = index + 10, column = 1, sticky = W)
                        r += 1
                

                Label(long_win, text = 'So, which fuction?', font = ('Segoe UI Light', 11)).grid(row = r + 1, column = 1, pady = 5, sticky = W)

                ttk.Button(long_win, text = 'Area', command = lambda: measure(1)).grid(row = r + 2, column = 5, pady = 5, sticky = W+E, padx = (0, 19))
                ttk.Button(long_win, text = 'Volume', command = lambda: measure(3)).grid(row = r + 2, column = 3, pady = 5, sticky = W+E)
                ttk.Button(long_win, text = 'Distance', command = lambda: measure(2)).grid(row = r + 2, column = 1, pady = 5, sticky = W+E)


        if value == 1:
            Label(long_win, text = 'X').grid(row = 4, column = 0, padx = 10, pady = 5)
            p1x = ttk.Entry(long_win)
            p1x.grid(row = 4, column = 1, padx = (0,10), sticky = E)
            Label(long_win, text = 'Y').grid(row = 5, column = 0, padx = 10, pady = 5)
            p1y = ttk.Entry(long_win)
            p1y.grid(row = 5, column = 1, padx = (0,10), sticky = E)
            Label(long_win, text = 'Z').grid(row = 6, column = 0, padx = 10, pady = 5)
            p1z = ttk.Entry(long_win)
            p1z.grid(row = 6, column = 1, padx = (0,10), sticky = E)
            #remind me to the destroy the ttk.Entry boxes
            n = ttk.Button(long_win, command = input_1).grid(row = 7, column = 0, columnspan = 2, sticky = W + E, padx = (10, 9), pady = 5)

        elif value == 2:
            Label(long_win, text = 'P1').grid(row = 4, column = 1)
            Label(long_win, text = 'X').grid(row = 5, column = 0, padx = 10, pady = 5)
            p1x = ttk.Entry(long_win)
            p1x.grid(row = 5, column = 1)
            Label(long_win, text = 'Y').grid(row = 6, column = 0, padx = 10, pady = 5)
            p1y = ttk.Entry(long_win)
            p1y.grid(row = 6, column = 1)
            Label(long_win, text = 'Z').grid(row = 7, column = 0, padx = 10, pady = 5)
            p1z = ttk.Entry(long_win)
            p1z.grid(row = 7, column = 1)
            Label(long_win, text = 'P2').grid(row = 4, column = 3)
            Label(long_win, text = 'X').grid(row = 5, column = 2, padx = 10, pady = 5)
            p2x = ttk.Entry(long_win)
            p2x.grid(row = 5, column = 3, padx = (0, 20))
            Label(long_win, text = 'Y').grid(row = 6, column = 2, padx = 10, pady = 5)
            p2y = ttk.Entry(long_win)
            p2y.grid(row = 6, column = 3, padx = (0, 20))
            Label(long_win, text = 'Z').grid(row = 7, column = 2, padx = 10, pady = 5)
            p2z = ttk.Entry(long_win)
            p2z.grid(row = 7, column = 3, padx = (0, 20))
            #remind me to the destroy the ttk.Entry boxes
            n = ttk.Button(long_win, command = input_2).grid(row = 8, column = 3, pady = (10, 20), padx = (0, 19), sticky = W + E)

        elif value == 3:
            Label(long_win, text = 'P1').grid(row = 4, column = 1)
            Label(long_win, text = 'X').grid(row = 5, column = 0, padx = 10, pady = 5)
            p1x = ttk.Entry(long_win)
            p1x.grid(row = 5, column = 1)
            Label(long_win, text = 'Y').grid(row = 6, column = 0, padx = 10, pady = 5)
            p1y = ttk.Entry(long_win)
            p1y.grid(row = 6, column = 1)
            Label(long_win, text = 'Z').grid(row = 7, column = 0, padx = 10, pady = 5)
            p1z = ttk.Entry(long_win)
            p1z.grid(row = 7, column = 1)
            Label(long_win, text = 'P2').grid(row = 4, column = 3)
            Label(long_win, text = 'X').grid(row = 5, column = 2, padx = 10, pady = 5)
            p2x = ttk.Entry(long_win)
            p2x.grid(row = 5, column = 3)
            Label(long_win, text = 'Y').grid(row = 6, column = 2, padx = 10, pady = 5)
            p2y = ttk.Entry(long_win)
            p2y.grid(row = 6, column = 3)
            Label(long_win, text = 'Z').grid(row = 7, column = 2, padx = 10, pady = 5)
            p2z = ttk.Entry(long_win)
            p2z.grid(row = 7, column = 3)
            Label(long_win, text = 'P3').grid(row = 4, column = 5)
            Label(long_win, text = 'X').grid(row = 5, column = 4, padx = 10, pady = 5)
            p3x = ttk.Entry(long_win)
            p3x.grid(row = 5, column = 5, padx = (0, 20))
            Label(long_win, text = 'Y').grid(row = 6, column = 4, padx = 10, pady = 5)
            p3y = ttk.Entry(long_win)
            p3y.grid(row = 6, column = 5, padx = (0, 20))
            Label(long_win, text = 'Z').grid(row = 7, column = 4, padx = 10, pady = 5)
            p3z = ttk.Entry(long_win)
            p3z.grid(row = 7, column = 5, padx = (0, 20))
            #remind me to the destroy the ttk.Entry boxes
            n = ttk.Button(long_win, command = input_3).grid(row = 8, column = 5, pady = (10,20), padx = (0, 19), sticky = W + E)
    inl = LabelFrame(root, text = 'Instructions', font = ('Segoe UI Light', 11, 'underline'))
    inl.grid(row = 4, column = 0, columnspan = 3, padx = 10)
    Label(
        inl,
        justify = 'left',
        text = 
        '- Input the co-ordinates of the points \n- You can use the same points to solve for different calcultions \n- In abscence of a particular co-ordinate use the number \'0\' \n- Do not use the 2/3-point system to perform calculations invlolving only 1/2 of the points \n(This has not been tested yet)',
        font = ('Segoe UI Light', 11)
    ).grid(row = 0, column = 0, padx = 10, sticky = W)
    Label(root, text = 'How many points are we dealing with?', font = ('Segoe UI Light', 11)).grid(row = 5, column = 0, columnspan = 4, padx = 10)
    Label(root, text = '(Please note that if only one point is supplied,\n all calculations will be done relative to the origin!)', font = ('arial', 10, 'italic'), foreground = 'grey').grid(row = 6, column = 0, columnspan = 4)
    b1 = ttk.Button(root, text = '1', command = lambda: no_of_points(1)).grid(row = 7, column = 0, padx = 10, pady = 10)
    b2 = ttk.Button(root, text = '2', command = lambda: no_of_points(2)).grid(row = 7, column = 1, padx = 10, pady = 10)
    b3 = ttk.Button(root, text = '3', command = lambda: no_of_points(3)).grid(row = 7, column = 2, padx = 10, pady = 10)
        
#Main window code
Label(root, text = '''This is a program to calculate stuff in a 3D plane.
Let's begin!''', font = ('Segoe UI Light', 11)).grid(row = 0, column = 0, columnspan = 3, padx = 10)

B1 = ttk.Button(root, command = longform)
B1.grid(row = 3, column = 1, padx = 10, pady = (10, 20))

root.mainloop()

'''
Stuff I still need to add
-How to deal with curved lines 
'''