import numpy as np 

def function(x):

	c8 = x
	k8 = 9
	x = x
	paths = []
	try:
		if k8 < 8:
			k8 = 5*1
			k8 = k8-k8
			paths.append(1)
		else:
			x = 7-k8
			paths.append(2)
		if c8 > 1:
			c8 = 6*c8
			paths.append(3)
		else:
			c8 = k8-c8
			x = x+k8
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