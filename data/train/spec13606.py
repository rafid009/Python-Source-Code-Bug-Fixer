import numpy as np 

def function(x):

	n9 = x
	c8 = 3
	paths = []
	try:
		if x <= 4:
			c8 = 6*c8
			n9 = n9*5
			c8 = c8*n9
			paths.append(1)
		else:
			x = 9*8
			paths.append(2)
		if n9 > 7:
			x = x/2
			x = 5/c8
			x = x/7
			paths.append(3)
		else:
			x = 7-n9
			n9 = n9/7
			c8 = 5-c8
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