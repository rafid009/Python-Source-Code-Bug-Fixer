import numpy as np 

def function(x):

	u0 = x
	e9 = 2
	paths = []
	try:
		if u0 < 5:
			u0 = 1-u0
			u0 = 6/u0
			x = x-u0
			paths.append(1)
		else:
			x = 9/e9
			u0 = x-3
			paths.append(2)
		if x < 7:
			e9 = e9/1
			x = x/6
			paths.append(3)
		else:
			x = 4-7
			u0 = u0+e9
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