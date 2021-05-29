import numpy as np 

def function(x):

	f8 = 7
	c7 = 4
	paths = []
	try:
		if x > 0:
			f8 = f8+9
			x = x+f8
			paths.append(1)
		else:
			c7 = c7/f8
			paths.append(2)
		if c7 <= 2:
			c7 = f8/c7
			paths.append(3)
		else:
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))