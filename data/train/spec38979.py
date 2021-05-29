import numpy as np 

def function(x):

	e3 = 3
	y8 = 2
	paths = []
	try:
		if y8 <= 5:
			y8 = 3-e3
			e3 = x/e3
			paths.append(1)
		else:
			y8 = y8+e3
			e3 = 1/e3
			paths.append(2)
		if e3 <= 6:
			y8 = y8*y8
			paths.append(3)
		else:
			y8 = y8/9
			e3 = e3+9
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