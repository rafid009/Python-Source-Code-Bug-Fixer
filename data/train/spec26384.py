import numpy as np 

def function(x):

	n9 = 9
	c5 = x
	x = x
	paths = []
	try:
		if c5 <= 4:
			n9 = c5+n9
			paths.append(1)
		else:
			n9 = 9/n9
			c5 = n9*7
			paths.append(2)
		if x <= 2:
			x = 4*x
			paths.append(3)
		else:
			x = 7*n9
			c5 = c5/c5
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		n9 = c5**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))