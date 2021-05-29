import numpy as np 

def function(x):

	c6 = 7
	k8 = x
	x = x
	paths = []
	try:
		if x <= 1:
			x = 2+x
			c6 = c6-c6
			paths.append(1)
		else:
			c6 = 2/c6
			paths.append(2)
		if x <= 0:
			x = 5+x
			x = k8+5
			x = x+k8
			paths.append(3)
		else:
			k8 = k8-3
			k8 = 2+k8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c6 = x**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))