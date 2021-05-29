import numpy as np 

def function(x):

	w4 = x
	c0 = x
	paths = []
	try:
		if w4 > 6:
			c0 = c0*7
			paths.append(1)
		else:
			w4 = w4-x
			w4 = 5+6
			w4 = 2/c0
			paths.append(2)
		if x <= 6:
			w4 = w4+7
			paths.append(3)
		else:
			c0 = c0+3
			w4 = x/7
			c0 = 5+x
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		w4 = c0**0.5
		return w4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))