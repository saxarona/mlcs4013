# dataset preprocessing

"""
I treated all files in order to get bigger dbs instead of 1k separated files.
Please read the docstrings of the functions.
The dataset is ready.
So am I.
"""

import os
import csv
import sys

dirname = os.getcwd()
path, scriptname = os.path.split(os.path.realpath(__file__))

mydata = []

mydir = os.listdir(dirname)
mydir.remove(scriptname)

# Standarize data
# This is because there was data separated by a single space
# and some other attributes were separated by a double space
# Terrible, if you ask me.


def standarize():
    """
    Standarize data files so that all of them are separated
    by a single space instead of a double space.
    """
    for filename in mydir:
        with open(filename, 'r') as file:
            filedata = file.read()

        filedata = filedata.replace('  ', ' ')

        with open(filename, 'w') as file:
            file.write(filedata)

        file.close()
    print("All files are now standarized.")


# With the data now standarized, we can begin to convert it to
# a single file in csv mode


def merge(mode):
    """
    Merge all data files into a single file.
    If mode is Full,all data entries are merged into a single file
    with classes attributes stated as 1:1 or 1:10.
    Otherwise, the mode argument describes which class should be marked as 1,
    and the rest of the classes are marked as -1 in the class att.
    """
    print("Running mode: {}".format(mode))

    for filename in mydir:
        with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile, delimiter=' ')

                try:
                    for row in reader:
                        # print(row)
                        aux = []
                        temp = row

                        if(mode == "Full"):
                            for index, att in enumerate(temp):
                                if(index != 1 and index != 2):
                                    aux.append(str(index+1) + ':' + att)
                                    mydata.append(aux)
                                    # print(aux)

                        else:
                            for index, att in enumerate(temp):
                                # Appending class attribute
                                if(index == 0):
                                    if(att == mode):
                                        aux.append("1")
                                    else:
                                        aux.append("-1")

                                # Appending the rest of the attributes
                                elif(index != 1 and index != 2):
                                    aux.append(str(index+1) + ':' + att)
                                    # print(aux)
                            mydata.append(aux)

                except csv.Error as e:
                    sys.exit('Eror wn')

    with open(mode + '_test.txt', 'w') as outfile:
        writer = csv.writer(outfile, delimiter=' ', lineterminator='\n')
        for line in mydata:
            writer.writerow(line)
    print("Done.\n Output file: {}_test.txt".format(mode))


# if this works, we can then replace every file

# for index, filename in enumerate(mydir):
#   with open(filename, 'w') as file:
#       file.write(' '.join(mydata[index]))

def main():
    # First we standarize
    # standarize()

    # Then we merge in different modes
    # Switch between modes,
    # e.g. merge(mode="1") will only consider class 1 and
    # assign -1 to all other classes in the class attribute
    merge(mode="10")
    


if __name__ == '__main__':
    main()
