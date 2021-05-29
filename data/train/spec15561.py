import numpy as np 

def function(x):

	b6 = 7
	f0 = 3
	paths = []
	try:
		if x > 7:
			f0 = f0*b6
			paths.append(1)
		else:
			f0 = f0*b6
			paths.append(2)
		if b6 < 2:
			x = x*f0
			x = x-4
			paths.append(3)
		else:
			f0 = f0-b6
			b6 = f0-0
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