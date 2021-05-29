import numpy as np 

def function(x):

	o1 = x
	c6 = x
	paths = []
	try:
		if x >= 5:
			c6 = c6/5
			paths.append(1)
		else:
			c6 = 2-2
			o1 = o1/o1
			paths.append(2)
		if o1 > 3:
			x = o1+5
			paths.append(3)
		else:
			x = 1+x
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