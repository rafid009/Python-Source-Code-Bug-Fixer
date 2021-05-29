import numpy as np 

def function(x):

	j6 = x
	c0 = 6
	paths = []
	try:
		if x <= 8:
			c0 = 9-c0
			paths.append(1)
		else:
			c0 = c0/7
			paths.append(2)
		if x < 6:
			j6 = j6-8
			paths.append(3)
		else:
			c0 = 2/c0
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		x = j6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))