import numpy as np 

def function(x):

	w4 = 0
	c3 = x
	paths = []
	try:
		if x >= 7:
			w4 = w4/x
			c3 = c3+2
			w4 = 2-w4
			paths.append(1)
		else:
			w4 = w4-x
			w4 = 2/w4
			w4 = 3/c3
			paths.append(2)
		if w4 < 4:
			x = x-4
			w4 = 1/w4
			x = 9-x
			paths.append(3)
		else:
			x = x*5
			x = x/2
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		x = c3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))