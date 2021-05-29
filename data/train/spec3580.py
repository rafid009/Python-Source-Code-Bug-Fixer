import numpy as np 

def function(x):

	a7 = x
	r9 = x
	paths = []
	try:
		if r9 > 9:
			r9 = 7*x
			paths.append(1)
		else:
			r9 = 3+6
			x = x-r9
			r9 = r9-r9
			paths.append(2)
		if a7 > 8:
			a7 = r9-7
			a7 = 2/a7
			paths.append(3)
		else:
			x = x/1
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