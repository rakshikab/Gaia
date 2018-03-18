import random
import os


def generate_matrix(rows, columns):
    """
    Create and return a matrix of WxH with a randomly generated values.
    
    Row 3, Column 2
    data = [
        [0.2558341468235693, 0.1933919029729071, 0.11110670143916135],
        [0.4457356172328676, 0.1022283066901275, 0.5198192889044888]
    ]
    
    :param width: 
    :param height: 
    :return: 
    """
    data = [[random.random() for x in range(rows)] for x in range(columns)]
    return data


def write_xyz(data, filename, path):
    """
    Write matrix into an XYZ file format.
    :param data: array
    :param filename: output xyz file name
    :param path: path to store the output xyz file
    :return: 
    """
    x = 0
    y = 0
    file_path = os.path.join(path, filename, ".xyz")

    print "Writing data to {path}...".format(path=file_path)

    with open(file_path, "w") as fh:
        fh.write("X Y Z\n")
        for column in data:
            for z in column:
                line = "{x} {y} {z}".format(x=x, y=y, z=z)
                fh.write(line)
                x += 1
                if x == len(data):
                    x = 0
                    y += 1

    print "XYZ file generated at {path}...".format(path=file_path)

