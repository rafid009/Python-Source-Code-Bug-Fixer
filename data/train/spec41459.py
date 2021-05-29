import numpy as np 

def function(x):

	a8 = 8
	c4 = 8
	paths = []
	try:
		if a8 < 0:
			a8 = 2+a8
			x = 0*8
			paths.append(1)
		else:
			a8 = a8*0
			c4 = 8*a8
			paths.append(2)
		if x > 9:
			x = 7*c4
			x = c4*5
			a8 = a8-3
			paths.append(3)
		else:
			c4 = c4/4
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