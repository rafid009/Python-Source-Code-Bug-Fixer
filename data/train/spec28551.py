import numpy as np 

def function(x):

	c6 = x
	k2 = 7
	paths = []
	try:
		if x <= 7:
			c6 = 9*c6
			c6 = c6/2
			k2 = k2+x
			paths.append(1)
		else:
			c6 = c6-4
			paths.append(2)
		if c6 < 6:
			k2 = k2/5
			x = c6-x
			paths.append(3)
		else:
			c6 = 4-c6
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		x = k2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))