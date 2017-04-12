# dataset preprocessing

"""
I treated all files in order to get 1 big db instead of 1k files.
The dataset is ready.
So am I.
"""

import os, csv, sys
dirname = os.getcwd()
path, scriptname = os.path.split(os.path.realpath(__file__))

mydata = []

# Standarize data
# This is because there was data separated by a single space
# and some other attributes were separated by a double space
# terrible, if you ask me.

mydir = os.listdir(dirname)
mydir.remove(scriptname)

for filename in mydir:
	with open(filename, 'r') as file:
		filedata = file.read()
	
	filedata = filedata.replace('  ', ' ')

	with open(filename, 'w') as file:
		file.write(filedata)

	file.close()


# With the data now standarized, we can begin to convert it to
# a single file in csv mode

for filename in mydir:
	with open(filename, 'r') as csvfile:
			reader = csv.reader(csvfile, delimiter=' ')
			try:
				for row in reader:
					print(row)
					aux = []
					temp = row
					for index, att in enumerate(temp):
						if (index != 1 and index != 2):
							aux.append(str(index+1) + ':' + att)
					print(aux)
					mydata.append(aux)
			except csv.Error as e:
				sys.exit('Eror wn')


# if this works, we can then replace every file

# for index, filename in enumerate(mydir):
# 	with open(filename, 'w') as file:
# 		file.write(' '.join(mydata[index]))

with open('all.txt', 'w') as outfile:
	writer = csv.writer(outfile, delimiter=' ')
	for line in mydata:
		writer.writerow(line)


print("Finished.")
input()

