import numpy as np 

def function(x):

	e8 = x
	j9 = 3
	paths = []
	try:
		if x > 5:
			e8 = 7/e8
			j9 = x/j9
			e8 = e8-8
			paths.append(1)
		else:
			e8 = e8/5
			paths.append(2)
		if e8 < 8:
			e8 = j9+j9
			paths.append(3)
		else:
			x = 7/x
			x = x-9
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