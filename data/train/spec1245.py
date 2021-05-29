import numpy as np 

def function(x):

	c2 = 2
	w6 = 9
	paths = []
	try:
		if c2 <= 2:
			w6 = 9/w6
			w6 = 0-w6
			c2 = 4-3
			paths.append(1)
		else:
			x = 2-3
			c2 = c2/7
			c2 = 8*x
			paths.append(2)
		if x >= 5:
			w6 = w6/w6
			w6 = 0-1
			paths.append(3)
		else:
			w6 = x*3
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		c2 = w6**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))