import numpy as np 

def function(x):

	a5 = x
	r9 = 5
	paths = []
	try:
		if r9 > 7:
			r9 = r9-2
			paths.append(1)
		else:
			a5 = 0/a5
			paths.append(2)
		if a5 > 8:
			x = r9+r9
			a5 = 1-x
			x = 1+x
			paths.append(3)
		else:
			a5 = r9+1
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