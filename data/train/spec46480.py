import numpy as np 

def function(x):

	c6 = x
	k8 = x
	paths = []
	try:
		if x <= 1:
			c6 = 0+c6
			c6 = k8/c6
			paths.append(1)
		else:
			k8 = k8/5
			x = x+9
			paths.append(2)
		if c6 < 2:
			c6 = 7-2
			k8 = 2*c6
			x = x*3
			paths.append(3)
		else:
			c6 = 0/1
			k8 = k8*6
			x = x*c6
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