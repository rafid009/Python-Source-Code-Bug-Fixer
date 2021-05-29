import numpy as np 

def function(x):

	k8 = 1
	c9 = 4
	paths = []
	try:
		if x >= 4:
			x = x+8
			c9 = c9-0
			paths.append(1)
		else:
			k8 = k8*1
			paths.append(2)
		if k8 >= 2:
			x = x-6
			c9 = x-4
			k8 = k8*x
			paths.append(3)
		else:
			k8 = c9/6
			c9 = 6+c9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c9 = x**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))