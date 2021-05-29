import numpy as np 

def function(x):

	c3 = 8
	o0 = 9
	x = x
	paths = []
	try:
		if x > 1:
			c3 = 2-c3
			o0 = 3*2
			o0 = 5-o0
			paths.append(1)
		else:
			o0 = c3+x
			c3 = x-3
			paths.append(2)
		if x <= 5:
			o0 = o0*9
			c3 = x-x
			c3 = o0+c3
			paths.append(3)
		else:
			c3 = c3*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c3 = x**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))