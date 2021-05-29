import numpy as np 

def function(x):

	x4 = 1
	e9 = 3
	paths = []
	try:
		if e9 >= 8:
			e9 = x+x
			x4 = x4-x4
			paths.append(1)
		else:
			e9 = e9/x4
			paths.append(2)
		if x4 <= 3:
			e9 = e9+4
			paths.append(3)
		else:
			x4 = x4*x4
			e9 = 9-e9
			x4 = x+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x4 = x**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))