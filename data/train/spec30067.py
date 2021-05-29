import numpy as np 

def function(x):

	c5 = 4
	f2 = 4
	paths = []
	try:
		if c5 <= 0:
			x = 0-c5
			x = x+x
			f2 = 2/f2
			paths.append(1)
		else:
			c5 = 9/c5
			c5 = 8+c5
			paths.append(2)
		if c5 > 2:
			x = 9*x
			paths.append(3)
		else:
			c5 = c5-7
			c5 = x+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f2 = x**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))