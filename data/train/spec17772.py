import numpy as np 

def function(x):

	k5 = 2
	c7 = x
	paths = []
	try:
		if c7 > 5:
			x = x+k5
			x = x+6
			k5 = k5+k5
			paths.append(1)
		else:
			x = x+c7
			k5 = x+8
			c7 = 4+c7
			paths.append(2)
		if k5 > 6:
			x = k5*x
			paths.append(3)
		else:
			x = x-0
			x = 6-8
			x = k5-4
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		x = c7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))