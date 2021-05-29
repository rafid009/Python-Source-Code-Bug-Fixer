import numpy as np 

def function(x):

	w9 = 2
	c6 = x
	paths = []
	try:
		if c6 >= 5:
			w9 = w9*8
			w9 = w9*7
			paths.append(1)
		else:
			w9 = w9/w9
			c6 = c6-2
			paths.append(2)
		if w9 > 8:
			x = x/5
			paths.append(3)
		else:
			w9 = w9+c6
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		c6 = w9**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))