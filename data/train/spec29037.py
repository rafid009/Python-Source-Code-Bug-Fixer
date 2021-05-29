import numpy as np 

def function(x):

	c6 = x
	k7 = x
	x = x
	paths = []
	try:
		if k7 <= 8:
			x = x-3
			paths.append(1)
		else:
			k7 = k7/k7
			paths.append(2)
		if c6 > 9:
			x = x*3
			paths.append(3)
		else:
			c6 = c6-c6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k7 = x**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))