import numpy as np 

def function(x):

	c4 = x
	d6 = x
	paths = []
	try:
		if c4 <= 7:
			c4 = 6*3
			d6 = x+3
			x = x+1
			paths.append(1)
		else:
			c4 = c4/d6
			d6 = d6*4
			d6 = 1*x
			paths.append(2)
		if x <= 7:
			x = x/x
			paths.append(3)
		else:
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))