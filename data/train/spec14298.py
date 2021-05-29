import numpy as np 

def function(x):

	d3 = 4
	a9 = 6
	paths = []
	try:
		if a9 < 1:
			a9 = 2*8
			a9 = 2/a9
			paths.append(1)
		else:
			a9 = 7-2
			paths.append(2)
		if d3 < 8:
			a9 = 0-9
			d3 = x-d3
			paths.append(3)
		else:
			a9 = 5-8
			a9 = 3-a9
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