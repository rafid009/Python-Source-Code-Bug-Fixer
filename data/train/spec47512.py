import numpy as np 

def function(x):

	w3 = x
	c0 = 4
	paths = []
	try:
		if x >= 2:
			x = 9+8
			paths.append(1)
		else:
			x = x/w3
			c0 = w3-5
			w3 = 0+w3
			paths.append(2)
		if c0 <= 7:
			c0 = w3-7
			c0 = 6-c0
			paths.append(3)
		else:
			c0 = c0/6
			c0 = 4/c0
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		x = c0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))