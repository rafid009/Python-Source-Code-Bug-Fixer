import numpy as np 

def function(x):

	v0 = x
	a9 = 9
	paths = []
	try:
		if a9 <= 1:
			a9 = a9*8
			v0 = v0+0
			paths.append(1)
		else:
			v0 = 7/v0
			v0 = v0*x
			paths.append(2)
		if a9 <= 6:
			x = x/a9
			paths.append(3)
		else:
			x = x+0
			x = 6*x
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