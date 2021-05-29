import numpy as np 

def function(x):

	c5 = x
	l7 = x
	paths = []
	try:
		if l7 >= 3:
			c5 = c5-0
			paths.append(1)
		else:
			c5 = c5*l7
			l7 = 9*l7
			paths.append(2)
		if l7 > 0:
			x = 2/3
			c5 = c5-x
			paths.append(3)
		else:
			c5 = 2/2
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		x = c5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))