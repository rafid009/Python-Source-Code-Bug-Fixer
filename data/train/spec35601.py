import numpy as np 

def function(x):

	v3 = x
	c3 = x
	paths = []
	try:
		if c3 > 6:
			v3 = c3-v3
			x = 4*9
			x = x-v3
			paths.append(1)
		else:
			c3 = 4+c3
			paths.append(2)
		if c3 < 1:
			x = 9/2
			v3 = 1*7
			paths.append(3)
		else:
			x = c3-3
			v3 = v3*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v3 = x**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))