import numpy as np 

def function(x):

	c5 = 3
	h3 = x
	paths = []
	try:
		if x >= 5:
			x = 7+3
			x = x+c5
			paths.append(1)
		else:
			x = 6*1
			x = x-5
			paths.append(2)
		if x > 9:
			x = x*h3
			paths.append(3)
		else:
			x = x/6
			c5 = h3/5
			c5 = c5+h3
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		c5 = h3**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))