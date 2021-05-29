import numpy as np 

def function(x):

	n9 = x
	c3 = 2
	paths = []
	try:
		if c3 <= 7:
			c3 = 4/2
			x = 7+x
			paths.append(1)
		else:
			c3 = c3+x
			c3 = 1/c3
			paths.append(2)
		if c3 < 5:
			x = x/x
			n9 = n9-8
			c3 = n9-c3
			paths.append(3)
		else:
			c3 = c3+c3
			c3 = n9+c3
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		x = n9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))