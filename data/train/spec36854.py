import numpy as np 

def function(x):

	o6 = 9
	c7 = x
	paths = []
	try:
		if x < 1:
			c7 = c7+1
			o6 = o6-x
			x = x/1
			paths.append(1)
		else:
			o6 = 8-o6
			c7 = o6*4
			paths.append(2)
		if o6 <= 0:
			o6 = 8/3
			paths.append(3)
		else:
			x = 4*x
			x = 2*x
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