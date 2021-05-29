import numpy as np 

def function(x):

	c4 = x
	a2 = 8
	paths = []
	try:
		if a2 >= 2:
			x = x*5
			paths.append(1)
		else:
			x = x/4
			c4 = c4+1
			paths.append(2)
		if a2 < 2:
			a2 = c4*x
			x = 3/x
			paths.append(3)
		else:
			c4 = 3*x
			a2 = x-5
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x = a2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))