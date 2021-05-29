import numpy as np 

def function(x):

	a2 = 5
	c7 = 9
	paths = []
	try:
		if x >= 2:
			a2 = a2*3
			paths.append(1)
		else:
			x = x/x
			x = x-5
			paths.append(2)
		if x > 4:
			x = 4+x
			paths.append(3)
		else:
			c7 = a2/c7
			c7 = c7*a2
			c7 = c7-3
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