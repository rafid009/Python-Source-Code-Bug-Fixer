import numpy as np 

def function(x):

	k8 = 4
	c9 = 6
	paths = []
	try:
		if k8 >= 8:
			c9 = 7*c9
			paths.append(1)
		else:
			k8 = 2*k8
			paths.append(2)
		if k8 <= 6:
			k8 = 1/c9
			k8 = 1+5
			paths.append(3)
		else:
			k8 = 4/6
			c9 = 4*c9
			k8 = k8*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k8 = x**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))