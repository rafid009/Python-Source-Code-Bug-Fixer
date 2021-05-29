import numpy as np 

def function(x):

	c7 = x
	a8 = x
	paths = []
	try:
		if a8 > 4:
			x = x+6
			x = 8-x
			paths.append(1)
		else:
			c7 = c7*8
			paths.append(2)
		if a8 < 5:
			a8 = x-c7
			paths.append(3)
		else:
			x = x*7
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