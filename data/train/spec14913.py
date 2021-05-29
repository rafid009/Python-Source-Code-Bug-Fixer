import numpy as np 

def function(x):

	a6 = x
	x9 = 0
	x = 5
	paths = []
	try:
		if x9 <= 8:
			x9 = x9-5
			x9 = x*8
			x9 = 2-x9
			paths.append(1)
		else:
			x = x-a6
			paths.append(2)
		if x <= 8:
			x = x9/x
			paths.append(3)
		else:
			x9 = 3+3
			a6 = 8+a6
			x9 = x9/5
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