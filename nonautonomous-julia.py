import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math
import mplcursors
import time

# Parameters
im_width, im_height = 1800, 1800
z_abs = 2
xmin, xmax = -2, 2
xwidth = xmax - xmin
ymin, ymax = -2, 2
yheight = ymax - ymin
# array to hold the different color values for the Julia set, initial values will be zero
julia = np.zeros((im_width, im_height))
fig, ax = plt.subplots()
number_user_inputs = 4
first_c_real_value = 0
first_c_imag_value = 0
second_c_real_value = 0
second_c_imag_value = 0
user_first_c_real_value = 0
user_first_c_imag_value = 0
user_second_c_real_value = 0
user_second_c_imag_value = 0
iterations_first_c_value = 15
user_iterations_first_c_value = 15
max_iteration_value = 125

"""View the Julia set for the nonautonomous complex dynamical system where the 
    first function being iterated over is z^2+first_c and the second function is z^2+second_c
    iterations_first_c is how many iterations of z^2+first_c will be done before doing z^2+second_c
    max_iteration is how many iterations of z^2+c we will do before assuming it goes to 0"""
def Nonautonomous_Julia_Set(first_c_real, first_c_imag, second_c_real, second_c_imag, iterations_first_c, max_iteration):
    first_c = complex(first_c_real, first_c_imag)
    second_c = complex(second_c_real, second_c_imag)
    for y in range(im_height):
        for x in range(im_width):
            # Find the point in the complex plane for the current pixel position
            z = complex(((x - im_width/2)*4/im_width), -((y - im_height/2)*4/im_height))
            iteration = 0
            # do the specified amount of iterations for the first function
            while (iteration < iterations_first_c) and (abs(z) <= z_abs):
                z = z**2 + first_c
                iteration += 1
            # finish off the rest of the iterations with the second function
            # if modulus of z > 2 then it will definitely go to infinity only check subsequent iterations if the modulus of # z <= 2
            while (abs(z) <= z_abs) and (iteration < max_iteration):
                z = z**2 + second_c
                iteration +=1
            # if it doesn't get beyond 2 for all the iterations assume it's bounded
            # need to switch x and y because of how computers deal with the coordinate system for pixels 
            if (iteration == max_iteration):
                julia[y, x] = 225
                # if it isn't bounded, color it such that the more iterations it takes to get beyond
                    #the lighter it gets colored
            else:
                julia[y, x] = math.floor((iteration/max_iteration) * 255)
    ax.imshow(julia, interpolation='nearest', cmap=cm.inferno)
    # Set the tick labels to the real coordinates in the complex plane ranging from xmin to xmax
    xtick_labels = np.linspace(xmin, xmax, xwidth + 1)
    ax.set_xticks([(x-xmin) / xwidth * im_width for x in xtick_labels])
    ax.set_xticklabels(['{:.1f}'.format(xtick) for xtick in xtick_labels])
    # Set the tick labels to the imaginary coordinates in the complex plane ranging from ymin to ymax
    ytick_labels = np.linspace(ymin, ymax, yheight + 1)
    ax.set_yticks([(y-ymin) / yheight * im_height for y in ytick_labels])
    # need to do -ytick because of how the y-axis is reversed
    ax.set_yticklabels(['{:.1f}'.format(-ytick) for ytick in ytick_labels])
    # crs = mplcursors.cursor(ax,hover=True)
    # Show the current point the user is hovering over
    # Need to switch the positives and negatives for the y-axis because of how the y-axis
        # is reversed
    # crs.connect("add", lambda sel: sel.annotation.set_text(
    #    '{} {} {}i'.format(round(((sel.target[0] - im_width/2)*4/im_width), 3), 
    #    ('' if round(((sel.target[1] - im_height/2)*4/im_height), 3) > 0 else '+'),
    #    round(-((sel.target[1] - im_height/2)*4/im_height), 3))))

def tellme(s):
    print(s)
    plt.title(s, fontsize=16)
    plt.draw() 

def user_input_c_values(order, type):
    repeat = True
    while(repeat):
        user_c_value = input("What would you like for the "+ type + " part of the c value for the " + type + " function of the sequence?" +
            " The number should be between -2 and 2.")
        stripped_c_value = user_c_value.replace("-", "")
        stripped_c_value = stripped_c_value.replace(".", "")
        if stripped_c_value.isnumeric():
            c_value = float(user_c_value)
            if c_value > 2 or c_value < -2:
                print("Please enter a number between -2 and 2.")
            else:
                return c_value
        else:
            print("You did not enter a number, please try again.")

def main():
    print("This program creates non-autonomous Julia sets where the functions in the sequence are of" + 
        " the form P(z) = z^2 + c.")
    user_first_c_real_value = user_input_c_values("first", "real")
    user_first_c_imag_value = user_input_c_values("first", "imaginary")
    user_second_c_real_value = user_input_c_values("second", "real")
    user_second_c_imag_value = user_input_c_values("second", "imaginary")
    repeat = True
    while(repeat):
        user_iterations_first_c_value = input("How many iterations would you like for the first function? This must be a positive integer.")
        stripped_iteration_value = user_iterations_first_c_value.replace("-", "")
        stripped_iteration_value = stripped_iteration_value.replace(".", "")
        if stripped_iteration_value.isnumeric():
            user_iterations_first_c_value = float(user_iterations_first_c_value)
            if (user_iterations_first_c_value <= 0) or (not user_iterations_first_c_value.is_integer()):
                print("Please enter a positive integer.")
            else:
                repeat = False
        else:
            print("You did not enter a number, please try again.")
    

    julia = Nonautonomous_Julia_Set(user_first_c_real_value, user_first_c_imag_value, user_second_c_real_value, user_second_c_imag_value, user_iterations_first_c_value, max_iteration_value)
    plt.draw() 
    plt.show()

if __name__ == "__main__":
    main()


