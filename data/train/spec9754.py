import numpy as np 

def function(x):

	c2 = x
	w4 = x
	x = x
	paths = []
	try:
		if w4 < 3:
			c2 = 1*c2
			x = x/x
			w4 = 8-w4
			paths.append(1)
		else:
			c2 = x-c2
			paths.append(2)
		if w4 > 1:
			w4 = 4-w4
			x = x-7
			x = x/w4
			paths.append(3)
		else:
			w4 = 4/w4
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		w4 = w4**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))