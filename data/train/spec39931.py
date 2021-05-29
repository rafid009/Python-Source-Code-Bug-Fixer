import numpy as np 

def function(x):

	c2 = x
	n9 = x
	paths = []
	try:
		if n9 >= 6:
			x = 5/x
			c2 = x/6
			paths.append(1)
		else:
			n9 = x*7
			n9 = 6/n9
			paths.append(2)
		if n9 > 1:
			n9 = n9/x
			c2 = c2-2
			c2 = 3+4
			paths.append(3)
		else:
			c2 = c2/1
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