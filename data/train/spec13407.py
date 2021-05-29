import numpy as np 

def function(x):

	f0 = 7
	c3 = x
	x = x
	paths = []
	try:
		if c3 <= 8:
			x = 8/x
			paths.append(1)
		else:
			f0 = 1*c3
			f0 = 2/9
			paths.append(2)
		if x < 4:
			c3 = 7-c3
			paths.append(3)
		else:
			c3 = 2/2
			c3 = 7*c3
			f0 = 3*f0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f0 = x**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))