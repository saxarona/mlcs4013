# dataset preprocessing

"""
I treated all files in order to get 1 big db instead of 1k files.
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
# terrible, if you ask me.


def standarize():
    """
    Standarize data files so that all of them are separated
    by a single space instad of double space.
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


def merge(mode="Full"):
    """
    Merge all data files into a single file.
    Default mode is Full, where all data entries are merged into a single file.
    Otherwise, mode describes which class should be included.
    """
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
                        else:
                            for index, att in enumerate(temp):
                                if(index == 0 and att == int(mode)):
                                    if(index != 1 and index != 2):
                                        aux.append(str(index+1) + ':' + att)
                        print(aux)
                        mydata.append(aux)

                except csv.Error as e:
                    sys.exit('Eror wn')

    with open(mode + '.txt', 'w') as outfile:
        writer = csv.writer(outfile, delimiter=' ')
        for line in mydata:
            writer.writerow(line)
    print("Done.\n Output file: %s.txt", mode)


# if this works, we can then replace every file

# for index, filename in enumerate(mydir):
#   with open(filename, 'w') as file:
#       file.write(' '.join(mydata[index]))

def main():
    merge("1") #let's try with a's

if __name__ == '__main__':
    main()
