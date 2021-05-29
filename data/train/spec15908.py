import numpy as np 

def function(x):

	c9 = 8
	f8 = x
	paths = []
	try:
		if f8 <= 4:
			f8 = 5-2
			paths.append(1)
		else:
			f8 = 9*f8
			c9 = c9*c9
			x = 2-x
			paths.append(2)
		if x < 6:
			x = x*f8
			x = x-0
			paths.append(3)
		else:
			f8 = f8/1
			x = x-c9
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