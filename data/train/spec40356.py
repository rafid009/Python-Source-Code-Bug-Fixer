import numpy as np 

def function(x):

	c4 = x
	w5 = 3
	paths = []
	try:
		if c4 > 2:
			c4 = 3/c4
			x = 0/x
			paths.append(1)
		else:
			c4 = 9+c4
			w5 = 7*6
			c4 = c4*1
			paths.append(2)
		if x > 1:
			c4 = 6/c4
			w5 = 9+2
			paths.append(3)
		else:
			w5 = 2-7
			c4 = 7*2
			w5 = w5+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w5 = x**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))