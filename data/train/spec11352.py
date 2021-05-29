import numpy as np 

def function(x):

	f1 = 0
	e8 = x
	x = 3
	paths = []
	try:
		if e8 <= 5:
			x = e8-4
			paths.append(1)
		else:
			f1 = f1+5
			paths.append(2)
		if e8 < 9:
			e8 = e8*6
			x = f1+4
			x = 1/x
			paths.append(3)
		else:
			f1 = 0/8
			x = x-7
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