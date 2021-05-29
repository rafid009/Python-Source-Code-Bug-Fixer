import numpy as np 

def function(x):

	d0 = x
	c4 = 6
	paths = []
	try:
		if x > 4:
			d0 = 1/d0
			d0 = 3+d0
			paths.append(1)
		else:
			c4 = c4-5
			paths.append(2)
		if d0 >= 4:
			c4 = 3/c4
			paths.append(3)
		else:
			c4 = 8-9
			x = x/3
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		d0 = c4**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))