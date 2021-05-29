import numpy as np 

def function(x):

	k3 = 7
	c5 = x
	paths = []
	try:
		if x < 0:
			k3 = 4-2
			paths.append(1)
		else:
			c5 = 2/c5
			paths.append(2)
		if x < 5:
			c5 = c5+1
			k3 = c5-2
			c5 = c5*8
			paths.append(3)
		else:
			c5 = c5+3
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