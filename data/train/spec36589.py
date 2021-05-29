import numpy as np 

def function(x):

	p7 = 1
	a7 = 7
	paths = []
	try:
		if x > 7:
			a7 = p7+3
			a7 = 2/a7
			p7 = x/2
			paths.append(1)
		else:
			x = x-3
			p7 = x+2
			paths.append(2)
		if a7 > 8:
			x = 4/p7
			p7 = p7/x
			paths.append(3)
		else:
			x = 1*x
			a7 = 9/p7
			x = x-1
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