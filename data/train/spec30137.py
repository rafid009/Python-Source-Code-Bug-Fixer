import numpy as np 

def function(x):

	a2 = 8
	c7 = x
	paths = []
	try:
		if a2 < 7:
			a2 = a2/a2
			paths.append(1)
		else:
			x = x*a2
			paths.append(2)
		if c7 < 3:
			a2 = 3+c7
			paths.append(3)
		else:
			a2 = 0-6
			c7 = c7/1
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