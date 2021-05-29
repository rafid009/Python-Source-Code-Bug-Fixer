import numpy as np 

def function(x):

	v0 = 9
	a2 = x
	paths = []
	try:
		if a2 > 1:
			v0 = 1-8
			x = 9+4
			a2 = a2+3
			paths.append(1)
		else:
			x = x-1
			a2 = x+3
			paths.append(2)
		if x > 2:
			v0 = 1+v0
			x = 6/x
			x = x+4
			paths.append(3)
		else:
			a2 = a2/2
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