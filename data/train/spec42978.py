import numpy as np 

def function(x):

	k3 = 7
	c5 = x
	paths = []
	try:
		if k3 >= 3:
			k3 = k3+6
			x = x/7
			paths.append(1)
		else:
			k3 = 3-1
			k3 = k3-x
			paths.append(2)
		if c5 > 1:
			c5 = 3+9
			k3 = 5-0
			paths.append(3)
		else:
			x = x*2
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