import numpy as np 

def function(x):

	c1 = x
	a3 = 4
	paths = []
	try:
		if x <= 8:
			a3 = x+a3
			c1 = 0*8
			paths.append(1)
		else:
			x = 9*c1
			paths.append(2)
		if a3 <= 7:
			x = x+5
			paths.append(3)
		else:
			x = a3-2
			a3 = a3/5
			a3 = 8-a3
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