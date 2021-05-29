import numpy as np 

def function(x):

	c2 = 6
	o0 = x
	paths = []
	try:
		if c2 > 2:
			o0 = c2+o0
			x = x*o0
			c2 = 5-3
			paths.append(1)
		else:
			c2 = 7/c2
			x = x-c2
			paths.append(2)
		if x < 8:
			x = x-o0
			x = x-o0
			x = x-9
			paths.append(3)
		else:
			x = x+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o0 = x**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))