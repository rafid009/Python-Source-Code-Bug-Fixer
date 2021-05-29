import numpy as np 

def function(x):

	w6 = x
	c1 = x
	paths = []
	try:
		if x > 2:
			w6 = c1*w6
			c1 = 0+c1
			x = x+9
			paths.append(1)
		else:
			c1 = 9*8
			paths.append(2)
		if c1 > 2:
			c1 = 9+0
			paths.append(3)
		else:
			c1 = c1/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w6 = x**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))