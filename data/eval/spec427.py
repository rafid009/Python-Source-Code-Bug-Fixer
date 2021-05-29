import numpy as np 

def function(x):

	c7 = 7
	w1 = x
	paths = []
	try:
		if w1 > 2:
			w1 = 2/8
			w1 = x*9
			paths.append(1)
		else:
			c7 = x-w1
			c7 = 8/w1
			paths.append(2)
		if c7 <= 1:
			c7 = c7+8
			c7 = 9*7
			paths.append(3)
		else:
			x = 5*c7
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		c7 = w1**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))