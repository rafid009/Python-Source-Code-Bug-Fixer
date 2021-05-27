import numpy as np 

def function(x):

	w5 = x
	c8 = 3
	paths = []
	try:
		if c8 > 9:
			w5 = w5/1
			w5 = w5+c8
			w5 = 9+c8
			paths.append(1)
		else:
			x = c8*7
			c8 = c8*x
			paths.append(2)
		if x <= 2:
			w5 = 2-w5
			paths.append(3)
		else:
			x = 7-1
			c8 = 6-x
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		c8 = w5**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))