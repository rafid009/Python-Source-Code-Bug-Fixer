import numpy as np 

def function(x):

	c2 = x
	c7 = x
	paths = []
	try:
		if c7 <= 3:
			c2 = c2-3
			c2 = c2-4
			c7 = 4+c7
			paths.append(1)
		else:
			x = c7+x
			x = 9+2
			paths.append(2)
		if c2 >= 6:
			c7 = x+c7
			paths.append(3)
		else:
			c7 = c7-6
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		x = c2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))