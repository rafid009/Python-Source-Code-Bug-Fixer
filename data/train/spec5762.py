import numpy as np 

def function(x):

	f0 = x
	v7 = x
	paths = []
	try:
		if x >= 7:
			v7 = x+v7
			x = x+1
			paths.append(1)
		else:
			f0 = f0/3
			paths.append(2)
		if v7 < 0:
			f0 = 8*f0
			x = x-4
			paths.append(3)
		else:
			f0 = f0*7
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