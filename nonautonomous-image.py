from PIL import Image 
import math

# Parameters
im_width, im_height = 2000, 2000, 
z_abs = 2
xmin, xmax = -2, 2
xwidth = xmax - xmin
ymin, ymax = -2, 2
yheight = ymax - ymin

def Julia(first_c_real, first_c_imag, second_c_real, second_c_imag, iterations_first_c, max_iteration):
    julia = Image.new("RGB", (im_width, im_height))
    first_c = complex(first_c_real, first_c_imag)
    second_c = complex(second_c_real, second_c_imag)
    for y in range(0, im_height):
        for x in range(0, im_width):
            z = complex(((x - im_width/2)*4/im_width), ((y - im_height/2)*4/im_height))
            iteration = 0
            # do the specified amount of iterations for the first function
            while (iteration < iterations_first_c) and (abs(z) <= 10000000):
                z = z**2 + first_c
                iteration += 1
            # finish off the rest of the iterations with the second function
            # if modulus of z > 2 then it will definitely go to infinity
            while (abs(z) <= z_abs) and (iteration < max_iteration):
                z = z**2 + second_c
                iteration +=1
            # if it doesn't get beyond 2 for all the iterations assume it's bounded
            if iteration == max_iteration:
                color = 255
            else:
                color = math.floor((iteration/max_iteration) * 255)
            julia.putpixel((x,y),(color,0,0))


    julia = julia.transpose(Image.FLIP_TOP_BOTTOM)
    julia.save('JuliaSet.png')
    julia.show()

myJulia = Julia(-1, 0, 0, 0, 12, 100)