import numpy as np 

def function(x):

	f4 = x
	c1 = 8
	paths = []
	try:
		if x > 1:
			x = x/2
			x = f4-2
			paths.append(1)
		else:
			x = 2*x
			x = f4/7
			paths.append(2)
		if c1 <= 0:
			x = 8-x
			paths.append(3)
		else:
			f4 = f4+c1
			f4 = 1/f4
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