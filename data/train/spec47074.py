import numpy as np 

def function(x):

	o4 = x
	s8 = x
	paths = []
	try:
		if x > 2:
			x = 1+2
			paths.append(1)
		else:
			o4 = x/o4
			x = 9*s8
			o4 = 6+o4
			paths.append(2)
		if x >= 0:
			o4 = o4-5
			paths.append(3)
		else:
			x = x-o4
			o4 = o4*s8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))