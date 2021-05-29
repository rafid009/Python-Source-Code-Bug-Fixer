import numpy as np 

def function(x):

	c3 = 8
	f5 = x
	paths = []
	try:
		if x > 5:
			c3 = c3/2
			f5 = 8+4
			f5 = f5+4
			paths.append(1)
		else:
			c3 = 0-c3
			paths.append(2)
		if c3 > 3:
			f5 = 8-c3
			x = 2*5
			paths.append(3)
		else:
			f5 = f5*x
			x = x+c3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f5 = x**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))