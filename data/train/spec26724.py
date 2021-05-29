import numpy as np 

def function(x):

	a1 = x
	p8 = 5
	x = 3
	paths = []
	try:
		if a1 < 2:
			x = 7/x
			paths.append(1)
		else:
			x = x+6
			p8 = p8/8
			paths.append(2)
		if a1 < 6:
			x = x-3
			paths.append(3)
		else:
			x = x/9
			a1 = a1/a1
			a1 = 2+a1
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