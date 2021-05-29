import numpy as np 

def function(x):

	f9 = 9
	c0 = 0
	paths = []
	try:
		if f9 >= 2:
			x = x*3
			x = x*f9
			paths.append(1)
		else:
			f9 = c0/1
			f9 = f9-1
			c0 = c0/6
			paths.append(2)
		if x <= 5:
			f9 = c0+f9
			f9 = f9-x
			paths.append(3)
		else:
			x = 1+f9
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