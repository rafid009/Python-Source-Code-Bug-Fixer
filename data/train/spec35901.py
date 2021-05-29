import numpy as np 

def function(x):

	c1 = x
	k0 = 9
	paths = []
	try:
		if k0 > 4:
			x = 1*x
			x = 5+x
			k0 = k0/c1
			paths.append(1)
		else:
			x = x+5
			paths.append(2)
		if c1 <= 0:
			c1 = c1/8
			k0 = c1/k0
			k0 = k0+c1
			paths.append(3)
		else:
			c1 = 4-2
			x = x*x
			x = x-9
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