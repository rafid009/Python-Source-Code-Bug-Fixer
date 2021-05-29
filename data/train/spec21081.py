import numpy as np 

def function(x):

	c7 = x
	k3 = 0
	paths = []
	try:
		if c7 > 0:
			c7 = x-9
			x = c7+0
			x = x/c7
			paths.append(1)
		else:
			k3 = 8/5
			paths.append(2)
		if k3 < 0:
			x = 4+x
			c7 = x+7
			paths.append(3)
		else:
			k3 = k3-x
			k3 = 3+c7
			c7 = 8-c7
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		x = k3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))