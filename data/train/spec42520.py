import numpy as np 

def function(x):

	k0 = 5
	c7 = x
	paths = []
	try:
		if c7 > 7:
			k0 = 2+k0
			c7 = 3/k0
			paths.append(1)
		else:
			k0 = c7*k0
			paths.append(2)
		if x <= 6:
			c7 = k0/c7
			paths.append(3)
		else:
			c7 = 3*4
			x = c7-x
			c7 = c7-k0
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		k0 = k0**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))