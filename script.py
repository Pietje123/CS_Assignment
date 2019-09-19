import csv
import matplotlib.pyplot as plt

file = 'istherecorrelation.csv'

beer = []
students = []
year = []


with open(file, 'r') as csvfile:
	csvfile.readline()
	henk = csv.reader(csvfile, delimiter=';')
	for i in henk:
		year.append(float(i[0]))
		students.append(float('.'.join(i[1].split(','))))
		beer.append(float(i[2])*1000)

plt.plot(year,beer)
# plt.plot(year,students)
plt.xlabel('Year ')
plt.ylabel('Beer (hL)')
plt.grid()
plt.savefig('plot.png', dpi = 300)