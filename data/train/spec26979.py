import numpy as np 

def function(x):

	f5 = 1
	g1 = 6
	paths = []
	try:
		if g1 < 3:
			g1 = 1-f5
			g1 = 8-g1
			paths.append(1)
		else:
			f5 = f5/2
			paths.append(2)
		if g1 <= 8:
			f5 = f5-5
			paths.append(3)
		else:
			x = x-4
			f5 = f5-f5
			f5 = x*f5
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