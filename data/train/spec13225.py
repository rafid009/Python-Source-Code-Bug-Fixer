import numpy as np 

def function(x):

	j1 = 2
	c0 = x
	paths = []
	try:
		if j1 < 3:
			x = x+2
			c0 = j1*7
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if j1 < 4:
			c0 = x*5
			paths.append(3)
		else:
			c0 = c0*x
			j1 = 4-j1
			c0 = c0/6
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