import numpy as np 

def function(x):

	x8 = x
	a3 = x
	paths = []
	try:
		if x > 3:
			x = 3+x
			x8 = 8/x8
			paths.append(1)
		else:
			a3 = 9-a3
			a3 = 5/a3
			paths.append(2)
		if x <= 2:
			a3 = a3-7
			a3 = a3/3
			a3 = a3/7
			paths.append(3)
		else:
			x = 8/x
			x = x/4
			x = a3/x
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