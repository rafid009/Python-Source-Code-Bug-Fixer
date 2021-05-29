import numpy as np 

def function(x):

	f2 = x
	e8 = 1
	paths = []
	try:
		if f2 <= 3:
			x = x-8
			paths.append(1)
		else:
			x = e8*3
			x = x/x
			paths.append(2)
		if x <= 9:
			e8 = 9*e8
			x = 8*x
			paths.append(3)
		else:
			f2 = 7+4
			x = 9+x
			e8 = e8*8
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