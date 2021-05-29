import numpy as np 

def function(x):

	k5 = 5
	c2 = 0
	paths = []
	try:
		if x < 6:
			k5 = c2-c2
			paths.append(1)
		else:
			k5 = k5-1
			c2 = k5-7
			paths.append(2)
		if c2 < 2:
			c2 = c2+c2
			c2 = c2*9
			paths.append(3)
		else:
			k5 = 4-8
			x = x-8
			c2 = c2+c2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k5 = x**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))