import numpy as np 

def function(x):

	l0 = x
	c7 = x
	paths = []
	try:
		if x > 0:
			c7 = 8+c7
			paths.append(1)
		else:
			l0 = 0*x
			paths.append(2)
		if x < 9:
			c7 = 0+c7
			paths.append(3)
		else:
			l0 = 1/l0
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		x = c7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))