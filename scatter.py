import random

def create_scatter(x, y, w, h, rows, columns, coefficient):
    """
    Utility which assumes RowsxColumns objects and gives back new coordinates for them after scattering
    :param x: Bottom left x-coordinate
    :param y: Bottom left y-coordinate
    :param w: Width of selection
    :param h: Height of selection
    :param rows: Number of objects in the x direction
    :param columns: Number of objects in the y direction
    :param coefficient: Randomness coefficient 0-1
    :return: 
    """

    xd = w*1.0/columns
    yd = h*1.0/rows
    print xd, yd
    scattered_tuples = []

    for ix in range(columns):
        for iy in range(rows):
            scattered_tuples.append(( x + (xd*ix) + random.uniform(-coefficient, coefficient)*xd,
                                      y + (yd*iy) + random.uniform(-coefficient, coefficient)*yd))

    return scattered_tuples