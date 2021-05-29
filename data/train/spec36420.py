import numpy as np 

def function(x):

	o1 = 4
	c1 = x
	paths = []
	try:
		if c1 > 8:
			x = x*x
			x = 0-3
			o1 = o1+x
			paths.append(1)
		else:
			c1 = c1-0
			paths.append(2)
		if x >= 6:
			c1 = x*x
			o1 = o1*8
			o1 = x/5
			paths.append(3)
		else:
			o1 = x*o1
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