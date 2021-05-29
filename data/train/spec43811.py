import numpy as np 

def function(x):

	c8 = x
	j7 = x
	x = x
	paths = []
	try:
		if x < 0:
			x = 8-5
			paths.append(1)
		else:
			x = j7/8
			paths.append(2)
		if x <= 9:
			x = x-5
			j7 = c8-x
			c8 = c8+c8
			paths.append(3)
		else:
			c8 = j7*2
			c8 = c8-j7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))