from tkinter import *
import math
import sys

def generate_fractal():
    sys.stdout.write('Generating fractal for c = {:.3f} + {:.3f}j...'.format(c.real,c.imag))
    sys.stdout.flush()
    for y in range(h):
        for x in range(w):
            z = centre + complex(((x-(w-1)/2.0)*pxw),(((h-1)/2.0-y)*pxw))
            n = 0
            while abs(z) < limit and n < 51:
                try:
                    z = pow(z,a) + c
                    n = n + 1
                except ZeroDivisionError:
                    z = limit
            pixel = int(255 * (0.5 + 0.5*math.cos(math.pi*n/51.0)))
            img.put('#{:02x}{:02x}{:02x}'.format(pixel,pixel,pixel),(x,y))
    sys.stdout.write('OK\n')
    sys.stdout.flush()

def set_z0(event):
    global z0
    z0 = complex((event.x - w/2) * pxw, (h/2 - event.y) * pxw)
    paint()

def set_c(event):
    global c
    c = complex((event.x - w/2) * pxw, (h/2 - event.y) * pxw)
    generate_fractal()
    paint()

def paint():
    canv.delete("all")
    canv.create_rectangle(0, 0, w, h, fill="white")
    canv.create_image((0,0), anchor="nw", image=img, state="normal")
    z = z0
    x = int(w/2 + z.real/pxw)
    y = int(h/2 - z.imag/pxw)
    canv.create_oval(x-3,y-3,x+4,y+4,fill="green")
    for n in range(100):
        p1 = z
        for m in range(M+2):
            if m <= M:
                p2 = pow(z,1.0+((a-1.0)*m)/M)
            else:
                p2 = p2 + c
            x1 = int(w/2 + p1.real / pxw)
            y1 = int(h/2 - p1.imag / pxw)
            x2 = int(w/2 + p2.real / pxw)
            y2 = int(h/2 - p2.imag / pxw)
            canv.create_line(x1, y1, x2, y2, fill="blue")
            p1 = p2
        z = pow(z,a) + c
        x = int(w/2 + z.real/pxw)
        y = int(h/2 - z.imag/pxw)
        canv.create_oval(x-3,y-3,x+4,y+4,fill="red")
        if (abs(z) > 10): break

# Create master Tk widget
master = Tk()
master.title('Julia Set Explorer - by Ted Burke - see http://batchloaf.com')

# Dimensions and resolution
w,h = 800,800
centre = 0 + 0j
pxw = 0.005

# Create Tk canvas widget
canv = Canvas(master, width=w, height=h)
canv.pack()
canv.bind("<B1-Motion>", set_z0)
canv.bind("<Button-1>",  set_z0)
canv.bind("<Button-2>",  set_c)
canv.bind("<Button-3>",  set_c) # this is actually the right click

# Iterating function parameters
a = 2.0
c = -0.12256 + 0.74486j
z0 = 0 + 0j
limit = 10

# Number of steps in plotting each curve within each orbit
M = 40

# Create image object to store Julia Set image
img = PhotoImage(width=w, height=h)

# Generate initial Julia Set image
generate_fractal()
paint()

# Main Tk event loop
mainloop()