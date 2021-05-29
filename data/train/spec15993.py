import numpy as np 

def function(x):

	c9 = 4
	w5 = 7
	paths = []
	try:
		if c9 > 8:
			c9 = c9-3
			c9 = 9*c9
			c9 = 0-c9
			paths.append(1)
		else:
			w5 = 0/2
			c9 = 6+w5
			w5 = c9+x
			paths.append(2)
		if w5 < 0:
			c9 = c9-9
			paths.append(3)
		else:
			c9 = c9/5
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		w5 = w5**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))