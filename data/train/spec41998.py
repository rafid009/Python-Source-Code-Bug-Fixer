import numpy as np 

def function(x):

	c3 = x
	n5 = 6
	paths = []
	try:
		if n5 <= 6:
			n5 = c3-n5
			paths.append(1)
		else:
			c3 = n5/n5
			n5 = 7/n5
			paths.append(2)
		if x <= 2:
			c3 = c3*6
			n5 = 4+n5
			paths.append(3)
		else:
			c3 = x+c3
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		x = n5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))