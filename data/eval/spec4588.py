import numpy as np 

def function(x):

	k0 = x
	c1 = 4
	paths = []
	try:
		if x <= 8:
			c1 = 0-c1
			k0 = k0*k0
			paths.append(1)
		else:
			k0 = 7-k0
			k0 = k0/5
			paths.append(2)
		if x <= 6:
			x = x/x
			c1 = x+x
			c1 = c1-k0
			paths.append(3)
		else:
			x = 9+7
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		x = c1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))