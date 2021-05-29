import numpy as np 

def function(x):

	c2 = 3
	k5 = x
	paths = []
	try:
		if k5 >= 1:
			k5 = 1/k5
			paths.append(1)
		else:
			x = x+0
			x = 6*x
			paths.append(2)
		if k5 <= 3:
			c2 = k5-c2
			paths.append(3)
		else:
			x = 3-x
			k5 = x*4
			c2 = 9*3
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		x = c2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))