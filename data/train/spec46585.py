import numpy as np 

def function(x):

	a5 = 2
	o4 = x
	paths = []
	try:
		if a5 <= 0:
			a5 = x/a5
			paths.append(1)
		else:
			a5 = 7+a5
			paths.append(2)
		if o4 > 6:
			x = x-0
			paths.append(3)
		else:
			a5 = a5-5
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