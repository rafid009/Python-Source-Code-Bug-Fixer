import numpy as np 

def function(x):

	q0 = x
	c0 = 9
	paths = []
	try:
		if c0 > 9:
			x = 1*x
			q0 = 6+q0
			paths.append(1)
		else:
			q0 = q0+9
			q0 = x-0
			paths.append(2)
		if q0 < 7:
			c0 = x-2
			paths.append(3)
		else:
			x = c0*x
			c0 = c0/c0
			x = x-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q0 = x**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))