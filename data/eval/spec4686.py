import numpy as np 

def function(x):

	n9 = 0
	c9 = 4
	paths = []
	try:
		if x <= 0:
			c9 = c9*c9
			x = 4*x
			paths.append(1)
		else:
			n9 = n9+n9
			n9 = n9+3
			paths.append(2)
		if n9 <= 9:
			n9 = 4+3
			c9 = c9-n9
			paths.append(3)
		else:
			x = c9+1
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		n9 = c9**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))