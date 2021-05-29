import numpy as np 

def function(x):

	y6 = 9
	c7 = x
	paths = []
	try:
		if y6 <= 4:
			y6 = 9+8
			paths.append(1)
		else:
			y6 = 3-5
			paths.append(2)
		if y6 >= 1:
			c7 = 2*5
			paths.append(3)
		else:
			x = c7-1
			x = c7+x
			x = 0*x
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