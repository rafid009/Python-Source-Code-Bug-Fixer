import numpy as np 

def function(x):

	w2 = x
	c9 = 9
	paths = []
	try:
		if x > 1:
			w2 = c9-x
			paths.append(1)
		else:
			w2 = 0*w2
			w2 = w2*6
			x = 9-x
			paths.append(2)
		if w2 >= 0:
			x = 4-x
			w2 = w2-2
			w2 = w2/3
			paths.append(3)
		else:
			c9 = c9/9
			w2 = w2/w2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c9 = x**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))