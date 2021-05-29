import numpy as np 

def function(x):

	a3 = 1
	d7 = 6
	paths = []
	try:
		if a3 >= 3:
			x = a3-x
			x = 1*d7
			paths.append(1)
		else:
			d7 = x-5
			d7 = d7+1
			a3 = a3+a3
			paths.append(2)
		if x >= 5:
			a3 = d7/x
			paths.append(3)
		else:
			a3 = 9+a3
			a3 = 5/a3
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