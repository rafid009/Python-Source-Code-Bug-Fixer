import numpy as np 

def function(x):

	q0 = 2
	a8 = 1
	paths = []
	try:
		if a8 < 6:
			q0 = q0*5
			x = q0/x
			paths.append(1)
		else:
			q0 = 8+q0
			a8 = 3-a8
			q0 = x+x
			paths.append(2)
		if q0 < 6:
			x = x-5
			q0 = q0/6
			q0 = 6*8
			paths.append(3)
		else:
			a8 = a8*7
			a8 = a8/q0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))