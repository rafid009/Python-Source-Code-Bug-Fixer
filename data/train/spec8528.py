import numpy as np 

def function(x):

	i8 = x
	r9 = 1
	paths = []
	try:
		if r9 > 9:
			i8 = 1-3
			paths.append(1)
		else:
			x = 2/1
			x = x+x
			x = 0-x
			paths.append(2)
		if r9 > 8:
			x = i8*x
			i8 = 8+r9
			x = 3*0
			paths.append(3)
		else:
			i8 = i8-x
			x = 7/x
			i8 = 3-i8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i8 = x**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))