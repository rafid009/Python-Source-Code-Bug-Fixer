import numpy as np 

def function(x):

	c8 = 5
	w6 = x
	paths = []
	try:
		if x < 6:
			c8 = x*1
			c8 = c8*7
			paths.append(1)
		else:
			w6 = 0*w6
			paths.append(2)
		if x < 8:
			x = 5+x
			paths.append(3)
		else:
			x = w6-x
			w6 = 2*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))