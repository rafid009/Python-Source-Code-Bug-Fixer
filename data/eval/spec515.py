import numpy as np 

def function(x):

	x9 = x
	e9 = 8
	paths = []
	try:
		if x9 <= 1:
			e9 = 4-e9
			x = x-5
			x = x*4
			paths.append(1)
		else:
			x9 = 2-x
			x = x/1
			x9 = x9+9
			paths.append(2)
		if x < 4:
			x9 = x9-x9
			paths.append(3)
		else:
			x9 = x*7
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