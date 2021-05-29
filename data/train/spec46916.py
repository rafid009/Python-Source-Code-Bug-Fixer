import numpy as np 

def function(x):

	k1 = 7
	c7 = 5
	paths = []
	try:
		if k1 <= 7:
			x = x-8
			c7 = 0/9
			paths.append(1)
		else:
			x = 0+9
			c7 = 3-c7
			c7 = c7/c7
			paths.append(2)
		if c7 >= 4:
			x = c7*x
			k1 = 4-k1
			k1 = k1+2
			paths.append(3)
		else:
			c7 = 2*k1
			k1 = 2-k1
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		c7 = k1**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))