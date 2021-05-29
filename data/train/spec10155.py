import numpy as np 

def function(x):

	c4 = 7
	e2 = x
	paths = []
	try:
		if c4 >= 4:
			e2 = x*e2
			e2 = 8*e2
			e2 = 0-0
			paths.append(1)
		else:
			x = 7+x
			x = x-5
			paths.append(2)
		if c4 <= 5:
			x = x/9
			x = 8-e2
			paths.append(3)
		else:
			x = c4*x
			e2 = 9*x
			e2 = e2+4
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