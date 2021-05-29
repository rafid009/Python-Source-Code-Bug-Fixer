import numpy as np 

def function(x):

	d5 = x
	c6 = x
	paths = []
	try:
		if d5 <= 8:
			c6 = 1/c6
			c6 = 8*c6
			d5 = d5*3
			paths.append(1)
		else:
			c6 = c6/2
			paths.append(2)
		if c6 > 0:
			c6 = c6*0
			x = 1+x
			x = x+d5
			paths.append(3)
		else:
			c6 = c6+d5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d5 = x**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))