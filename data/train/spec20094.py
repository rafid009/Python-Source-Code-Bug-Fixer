import numpy as np 

def function(x):

	c1 = x
	k2 = x
	x = 5
	paths = []
	try:
		if k2 < 7:
			k2 = 4*k2
			c1 = c1+2
			paths.append(1)
		else:
			k2 = 9*k2
			x = 1+0
			x = x-8
			paths.append(2)
		if c1 > 3:
			c1 = c1+c1
			paths.append(3)
		else:
			c1 = 6-3
			x = k2*3
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		k2 = k2**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))