import numpy as np 

def function(x):

	r1 = x
	a0 = 2
	paths = []
	try:
		if a0 > 0:
			x = 3-4
			x = 1/9
			paths.append(1)
		else:
			a0 = a0*r1
			paths.append(2)
		if a0 > 1:
			x = x-9
			paths.append(3)
		else:
			a0 = a0*r1
			x = x-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r1 = x**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))