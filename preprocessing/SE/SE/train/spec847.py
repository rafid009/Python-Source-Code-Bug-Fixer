import numpy as np 

def function(x):

	w5 = x
	c2 = x
	paths = []
	try:
		if x < 7:
			w5 = 5+w5
			c2 = 0/c2
			paths.append(1)
		else:
			c2 = c2-9
			paths.append(2)
		if x < 3:
			x = x-x
			paths.append(3)
		else:
			x = x+x
			c2 = c2*4
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		c2 = w5**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))