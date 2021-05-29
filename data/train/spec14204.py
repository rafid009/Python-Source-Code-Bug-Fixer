import numpy as np 

def function(x):

	o8 = 7
	a9 = 3
	paths = []
	try:
		if o8 < 8:
			x = 3/x
			o8 = 4*o8
			paths.append(1)
		else:
			x = x+o8
			x = x+9
			x = 0-3
			paths.append(2)
		if a9 < 2:
			a9 = a9/x
			a9 = 5-a9
			o8 = a9*8
			paths.append(3)
		else:
			a9 = o8*a9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))