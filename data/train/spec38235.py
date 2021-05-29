import numpy as np 

def function(x):

	c2 = 1
	n9 = x
	paths = []
	try:
		if c2 >= 7:
			n9 = 7+n9
			c2 = c2/7
			c2 = c2/x
			paths.append(1)
		else:
			x = 8*8
			n9 = n9-5
			n9 = 7-n9
			paths.append(2)
		if x >= 1:
			n9 = n9/6
			paths.append(3)
		else:
			x = 5/5
			n9 = n9/2
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		n9 = n9**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))