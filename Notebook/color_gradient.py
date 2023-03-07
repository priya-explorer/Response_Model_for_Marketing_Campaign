import numpy as np

def hex_to_rgb(hex_str):
    """ #FFFFFF -> [255,255,255]
    #Pass 16 to the integer function for change of base"""
    return [int(hex_str[i:i+2], 16) for i in range(1,6,2)]

def get_color_gradient(c1, c2, n):
    """
    c1,c2 (hex) : two hex colors
    n (int) : n colors
    returns : a color gradient
    """
    assert n > 1
    c1_rgb = np.array(hex_to_rgb(c1))/255
    c2_rgb = np.array(hex_to_rgb(c2))/255
    mix_pts = [x/(n-1) for x in range(n)]
    rgb_colors = [((1-mix)*c1_rgb + (mix*c2_rgb)) for mix in mix_pts]
    return ["#" + "".join([format(int(round(val*255)), "02x") for val in item]) for item in rgb_colors]
