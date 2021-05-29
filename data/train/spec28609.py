import numpy as np 

def function(x):

	x3 = x
	f7 = x
	paths = []
	try:
		if f7 < 3:
			f7 = 2*f7
			f7 = x3/3
			paths.append(1)
		else:
			x = x-8
			f7 = 2-x3
			paths.append(2)
		if x <= 2:
			f7 = 1/5
			paths.append(3)
		else:
			f7 = f7-4
			x3 = 5/x3
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