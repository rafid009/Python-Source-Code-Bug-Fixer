import numpy as np 

def function(x):

	k7 = x
	c4 = 1
	x = 4
	paths = []
	try:
		if x < 6:
			x = 5/x
			x = x+2
			paths.append(1)
		else:
			c4 = c4-5
			paths.append(2)
		if k7 >= 8:
			x = x/9
			x = x-4
			paths.append(3)
		else:
			c4 = 0/c4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k7 = x**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))