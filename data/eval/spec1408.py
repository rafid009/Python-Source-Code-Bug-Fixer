import numpy as np 

def function(x):

	k7 = 4
	c3 = x
	paths = []
	try:
		if x > 5:
			k7 = k7/9
			x = x*3
			x = x+4
			paths.append(1)
		else:
			k7 = k7/k7
			x = x*k7
			paths.append(2)
		if k7 > 2:
			x = x-k7
			c3 = c3+7
			c3 = c3/c3
			paths.append(3)
		else:
			c3 = 1-k7
			x = x-6
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