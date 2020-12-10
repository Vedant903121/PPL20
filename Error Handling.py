try:
	print(x)
except NameError:
	print("The name x is not defined")

try:
	print(int('4.1'))
except ValueError:
	print(int('4'))
