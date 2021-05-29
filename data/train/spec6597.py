import numpy as np 

def function(x):

	i8 = 4
	f9 = 1
	paths = []
	try:
		if i8 <= 0:
			i8 = f9+9
			paths.append(1)
		else:
			i8 = x-i8
			i8 = i8-1
			i8 = i8-9
			paths.append(2)
		if x >= 6:
			f9 = f9+2
			i8 = 8+i8
			paths.append(3)
		else:
			f9 = 0*f9
			i8 = i8*2
			f9 = 1*f9
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		i8 = i8**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))