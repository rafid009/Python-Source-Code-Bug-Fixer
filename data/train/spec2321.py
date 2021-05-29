import numpy as np 

def function(x):

	e4 = 8
	k0 = x
	paths = []
	try:
		if e4 <= 2:
			x = 6+k0
			k0 = k0-k0
			paths.append(1)
		else:
			k0 = 9*7
			e4 = 7+x
			e4 = x*4
			paths.append(2)
		if k0 > 1:
			x = 6/x
			paths.append(3)
		else:
			k0 = k0+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e4 = x**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))