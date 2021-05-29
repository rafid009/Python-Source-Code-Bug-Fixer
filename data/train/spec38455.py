import numpy as np 

def function(x):

	c7 = x
	a1 = x
	x = 1
	paths = []
	try:
		if x < 4:
			x = 4*1
			c7 = 2-c7
			paths.append(1)
		else:
			x = x/a1
			paths.append(2)
		if a1 < 1:
			x = 5/c7
			paths.append(3)
		else:
			x = 3/x
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