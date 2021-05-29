import numpy as np 

def function(x):

	c2 = x
	d7 = x
	paths = []
	try:
		if x <= 6:
			d7 = x+d7
			paths.append(1)
		else:
			x = 5-x
			d7 = 3*d7
			paths.append(2)
		if d7 >= 2:
			x = 8/d7
			paths.append(3)
		else:
			c2 = x/1
			c2 = 1-c2
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		d7 = d7**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))