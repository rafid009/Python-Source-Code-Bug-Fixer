import numpy as np 

def function(x):

	n3 = 2
	c3 = x
	paths = []
	try:
		if c3 < 1:
			x = x+x
			paths.append(1)
		else:
			n3 = 5/n3
			paths.append(2)
		if x < 7:
			x = x+7
			paths.append(3)
		else:
			n3 = n3-x
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		c3 = n3**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))