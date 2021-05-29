import numpy as np 

def function(x):

	w4 = x
	c7 = 7
	paths = []
	try:
		if c7 < 0:
			w4 = 9*7
			c7 = c7/c7
			paths.append(1)
		else:
			w4 = c7*1
			paths.append(2)
		if x > 3:
			w4 = 4+w4
			paths.append(3)
		else:
			w4 = x*9
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