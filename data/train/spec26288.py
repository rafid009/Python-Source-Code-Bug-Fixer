import numpy as np 

def function(x):

	c5 = x
	d6 = 8
	paths = []
	try:
		if d6 <= 7:
			d6 = c5-c5
			c5 = 9+d6
			d6 = d6-c5
			paths.append(1)
		else:
			x = c5*d6
			d6 = 0*6
			d6 = 7/8
			paths.append(2)
		if x < 0:
			c5 = c5+5
			d6 = 9/6
			paths.append(3)
		else:
			d6 = d6/2
			d6 = 4-d6
			c5 = c5-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))