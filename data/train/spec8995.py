import numpy as np 

def function(x):

	v0 = 7
	a3 = 0
	paths = []
	try:
		if x <= 0:
			x = 4-7
			x = x-9
			paths.append(1)
		else:
			v0 = 9+a3
			a3 = a3*9
			v0 = a3-3
			paths.append(2)
		if a3 > 4:
			x = 7*x
			v0 = 3-6
			a3 = a3/a3
			paths.append(3)
		else:
			x = x+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))