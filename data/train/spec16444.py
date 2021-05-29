import numpy as np 

def function(x):

	c8 = 7
	n9 = 9
	paths = []
	try:
		if n9 >= 7:
			n9 = 7*5
			paths.append(1)
		else:
			x = x*x
			x = 1*x
			x = x/9
			paths.append(2)
		if x > 1:
			c8 = 5-c8
			paths.append(3)
		else:
			n9 = 9-n9
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