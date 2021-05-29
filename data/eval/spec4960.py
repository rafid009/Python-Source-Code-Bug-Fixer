import numpy as np 

def function(x):

	c7 = x
	a5 = 1
	paths = []
	try:
		if c7 >= 1:
			c7 = 5/c7
			paths.append(1)
		else:
			a5 = a5/3
			paths.append(2)
		if c7 <= 6:
			a5 = c7*8
			paths.append(3)
		else:
			c7 = c7-x
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		a5 = a5**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))