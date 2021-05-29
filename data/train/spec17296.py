import numpy as np 

def function(x):

	f9 = 2
	i8 = 6
	paths = []
	try:
		if f9 >= 5:
			f9 = f9*f9
			paths.append(1)
		else:
			i8 = 6-i8
			f9 = 7+f9
			i8 = 0-i8
			paths.append(2)
		if i8 < 8:
			i8 = i8*3
			paths.append(3)
		else:
			i8 = 7+i8
			i8 = i8+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f9 = x**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))