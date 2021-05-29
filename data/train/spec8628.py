import numpy as np 

def function(x):

	c2 = 4
	k3 = 9
	paths = []
	try:
		if c2 > 3:
			c2 = 8+c2
			k3 = x+c2
			paths.append(1)
		else:
			c2 = 2-c2
			x = 6+7
			x = x-c2
			paths.append(2)
		if k3 >= 2:
			x = x/3
			paths.append(3)
		else:
			k3 = k3-9
			c2 = 0-c2
			k3 = k3/1
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		c2 = k3**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))