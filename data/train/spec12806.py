import numpy as np 

def function(x):

	a9 = x
	x8 = x
	paths = []
	try:
		if x8 <= 4:
			a9 = 3*x8
			x = 2/5
			paths.append(1)
		else:
			a9 = a9*6
			x = x-3
			paths.append(2)
		if x >= 9:
			x8 = x*x8
			x8 = x8*2
			paths.append(3)
		else:
			x = x-9
			a9 = 9/7
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