import numpy as np 

def function(x):

	c5 = 2
	a2 = 0
	paths = []
	try:
		if a2 >= 2:
			a2 = x*a2
			x = x+c5
			paths.append(1)
		else:
			x = 3+x
			c5 = c5*1
			c5 = c5-x
			paths.append(2)
		if x >= 3:
			c5 = c5/8
			paths.append(3)
		else:
			c5 = c5-x
			x = 6*x
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