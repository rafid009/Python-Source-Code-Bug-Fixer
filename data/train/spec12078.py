import numpy as np 

def function(x):

	k8 = 7
	c2 = 4
	paths = []
	try:
		if x <= 2:
			k8 = c2/k8
			x = x-9
			paths.append(1)
		else:
			x = x-6
			x = x-2
			c2 = 3-x
			paths.append(2)
		if k8 >= 6:
			x = 1-x
			k8 = k8+x
			paths.append(3)
		else:
			k8 = 7*6
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