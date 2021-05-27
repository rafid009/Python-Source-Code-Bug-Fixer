import numpy as np 

def function(x):

	f0 = x
	a6 = 6
	paths = []
	try:
		if a6 < 0:
			f0 = f0*7
			paths.append(1)
		else:
			f0 = f0*7
			x = f0+x
			a6 = 4*a6
			paths.append(2)
		if x < 8:
			a6 = 2*a6
			f0 = f0-f0
			paths.append(3)
		else:
			f0 = a6/a6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f0 = x**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))