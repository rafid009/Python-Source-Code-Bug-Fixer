import numpy as np 

def function(x):

	k0 = x
	c7 = x
	paths = []
	try:
		if x <= 9:
			x = x+8
			x = 1+8
			paths.append(1)
		else:
			c7 = x+9
			paths.append(2)
		if c7 <= 4:
			c7 = c7/4
			x = 9-k0
			x = x-8
			paths.append(3)
		else:
			k0 = k0+9
			x = 9+k0
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		k0 = c7**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))