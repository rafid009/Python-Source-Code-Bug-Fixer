import numpy as np 

def function(x):

	a9 = 9
	d1 = 0
	paths = []
	try:
		if a9 >= 6:
			x = x+9
			x = d1-x
			paths.append(1)
		else:
			a9 = 9+a9
			x = x/d1
			d1 = x-x
			paths.append(2)
		if d1 < 5:
			a9 = 6*a9
			x = x-d1
			x = x+6
			paths.append(3)
		else:
			a9 = 3/7
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