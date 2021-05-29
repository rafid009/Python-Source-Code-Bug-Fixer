import numpy as np 

def function(x):

	n5 = x
	c7 = 6
	paths = []
	try:
		if n5 > 8:
			x = x*8
			c7 = x/c7
			paths.append(1)
		else:
			c7 = 5/6
			x = 7*6
			paths.append(2)
		if n5 <= 8:
			n5 = n5+c7
			paths.append(3)
		else:
			n5 = n5*c7
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n5 = x**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))