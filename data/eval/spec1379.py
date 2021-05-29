import numpy as np 

def function(x):

	c4 = 1
	w2 = x
	x = 7
	paths = []
	try:
		if x >= 6:
			c4 = 0*c4
			paths.append(1)
		else:
			w2 = 8-1
			paths.append(2)
		if x >= 0:
			w2 = x/w2
			c4 = c4/4
			c4 = w2-0
			paths.append(3)
		else:
			w2 = x*w2
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		c4 = c4**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))