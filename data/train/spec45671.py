import numpy as np 

def function(x):

	i8 = x
	x7 = 8
	paths = []
	try:
		if x7 <= 7:
			x7 = i8*6
			x7 = 2*2
			paths.append(1)
		else:
			x7 = 6-x7
			x = x-4
			x = 7/i8
			paths.append(2)
		if x7 <= 6:
			x7 = i8/i8
			paths.append(3)
		else:
			x = x*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x7 = x**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))