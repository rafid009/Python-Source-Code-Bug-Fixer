import numpy as np 

def function(x):

	w3 = x
	c6 = 4
	paths = []
	try:
		if c6 < 4:
			w3 = 3*4
			w3 = 8+7
			paths.append(1)
		else:
			w3 = 1-w3
			paths.append(2)
		if c6 > 0:
			w3 = w3-c6
			x = 6-9
			c6 = 4+c6
			paths.append(3)
		else:
			c6 = c6-x
			c6 = w3*c6
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		x = w3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))