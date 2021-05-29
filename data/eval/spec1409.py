import numpy as np 

def function(x):

	k3 = x
	c6 = x
	paths = []
	try:
		if x >= 9:
			k3 = k3*8
			paths.append(1)
		else:
			k3 = k3+6
			c6 = c6-8
			c6 = c6-8
			paths.append(2)
		if k3 >= 8:
			c6 = x-c6
			paths.append(3)
		else:
			k3 = k3*3
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		x = c6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))