import numpy as np 

def function(x):

	c0 = x
	w5 = 9
	paths = []
	try:
		if c0 <= 0:
			w5 = 2*w5
			c0 = c0*4
			paths.append(1)
		else:
			x = x-5
			c0 = 7*9
			x = 4-x
			paths.append(2)
		if x > 9:
			c0 = w5-c0
			paths.append(3)
		else:
			w5 = c0+c0
			c0 = w5/c0
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