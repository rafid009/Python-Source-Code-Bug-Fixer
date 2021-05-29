import numpy as np 

def function(x):

	r0 = x
	e7 = x
	paths = []
	try:
		if x < 5:
			x = x-e7
			r0 = 2/r0
			paths.append(1)
		else:
			x = 2*r0
			paths.append(2)
		if x < 6:
			r0 = 9-7
			r0 = 3-r0
			paths.append(3)
		else:
			e7 = 3*4
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		x = e7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))