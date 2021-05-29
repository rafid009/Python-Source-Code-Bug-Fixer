import numpy as np 

def function(x):

	e2 = 0
	x5 = 4
	paths = []
	try:
		if x > 6:
			e2 = e2+2
			paths.append(1)
		else:
			x = x+5
			x = 9-8
			x = x-5
			paths.append(2)
		if x5 < 9:
			e2 = e2-0
			paths.append(3)
		else:
			x = 5-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x5 = x**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))