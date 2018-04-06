filename='pi_digits.txt'

with open(filename) as file_object:

	for lines_2 in file_object:
		print(lines_2.replace('Python','ccc'))
with open(filename) as file_object:
	lines=file_object.read()
	print(lines)
with open(filename) as file_object:
	lines_3=file_object.readlines()
	for n in lines_3:
		print(n)


