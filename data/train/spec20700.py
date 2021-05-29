import numpy as np 

def function(x):

	c2 = 5
	f1 = 1
	paths = []
	try:
		if x > 7:
			c2 = 0+x
			paths.append(1)
		else:
			f1 = f1/6
			f1 = f1/f1
			paths.append(2)
		if x < 8:
			f1 = x-3
			c2 = f1-8
			paths.append(3)
		else:
			x = 9*x
			c2 = c2*f1
			f1 = x/f1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))