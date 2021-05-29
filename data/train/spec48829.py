import numpy as np 

def function(x):

	z1 = 1
	a9 = x
	paths = []
	try:
		if z1 <= 0:
			x = a9-x
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if z1 < 8:
			x = x-5
			a9 = 1/a9
			paths.append(3)
		else:
			a9 = a9*x
			a9 = a9/5
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		x = a9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))