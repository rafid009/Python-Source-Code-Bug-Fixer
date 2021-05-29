import numpy as np 

def function(x):

	e7 = x
	a2 = 1
	paths = []
	try:
		if e7 < 7:
			x = 3-6
			a2 = a2*8
			a2 = a2*4
			paths.append(1)
		else:
			x = x-6
			x = 0/9
			a2 = 6-x
			paths.append(2)
		if a2 >= 0:
			e7 = 4+6
			e7 = 2*4
			paths.append(3)
		else:
			a2 = e7-x
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