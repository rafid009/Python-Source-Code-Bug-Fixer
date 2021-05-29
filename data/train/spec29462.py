import numpy as np 

def function(x):

	c0 = 5
	w4 = x
	paths = []
	try:
		if c0 > 5:
			x = 0*2
			paths.append(1)
		else:
			x = w4-x
			paths.append(2)
		if w4 < 4:
			x = c0+5
			paths.append(3)
		else:
			c0 = 6*c0
			x = x/3
			c0 = c0-5
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		x = w4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))