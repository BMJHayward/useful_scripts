from numpy import sin

def RGB_colour(r, g, b):
    return int('{}{}{}'.format(int(r), int(g), int(b)))

def colour_gradient(frq1, frq2, frq3, phs1, phs2, phs3, cntr=128, wdth=127, lnth=50):
    # eg: colour_gradient(.3,.3,.3,0,2,4) will produce a lovely rainbow
    for i in range(lnth):
        red   = np.sin(frq1 * i + phs1) * wdth + cntr
        green = np.sin(frq2 * i + phs2) * wdth + cntr
        blue  = np.sin(frq3 * i + phs3) * wdth + cntr
        yield RGB_colour(red, green, blue)

