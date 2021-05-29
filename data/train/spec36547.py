import numpy as np 

def function(x):

	b7 = 7
	k1 = 3
	x = x
	paths = []
	try:
		if b7 < 7:
			b7 = x-9
			paths.append(1)
		else:
			k1 = 4*x
			b7 = 9+4
			paths.append(2)
		if x > 0:
			x = x-3
			b7 = 1-9
			paths.append(3)
		else:
			x = 5*k1
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