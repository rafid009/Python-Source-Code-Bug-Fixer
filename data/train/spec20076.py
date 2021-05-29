import numpy as np 

def function(x):

	w2 = 2
	c0 = 3
	paths = []
	try:
		if c0 < 2:
			c0 = c0+9
			w2 = w2*9
			paths.append(1)
		else:
			w2 = 6*8
			c0 = w2+c0
			c0 = w2*0
			paths.append(2)
		if c0 >= 1:
			c0 = c0*x
			paths.append(3)
		else:
			w2 = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c0 = x**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))